from django.shortcuts import get_object_or_404, render, redirect
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from .forms import CadastroForm
from .models import Perfil, Filme
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.decorators import login_required


@login_required 
@login_required 
def home(request):
    # 1. Primeiro, verifica com segurança se o usuário logado tem e-mail confirmado
    if hasattr(request.user, 'perfil'):
        if not request.user.perfil.email_confirmado:
            return render(request, 'aguardando_confirmacao.html')
        perfil = request.user.perfil
    else:
        perfil = None 
            
    # 2. Busca TODOS os filmes no banco de dados inicialmente
    filmes = Filme.objects.all()
    
    # --- INÍCIO DO SISTEMA DE FILTROS E BUSCA ---
    busca_nome = request.GET.get('pesquisa')
    filtro_genero = request.GET.get('genero')
    filtro_ano = request.GET.get('ano')
    filtro_avaliacao = request.GET.get('avaliacao')

    # Filtro por Nome (Barra de Pesquisa)
    if busca_nome:
        filmes = filmes.filter(titulo__icontains=busca_nome)

    # Filtro por Gênero
    if filtro_genero:
        filmes = filmes.filter(genero__iexact=filtro_genero)

    # Filtro por Ano
    if filtro_ano:
        if filtro_ano == 'antigos':
            filmes = filmes.filter(ano__lt=2024)  # Menor que 2024
        else:
            filmes = filmes.filter(ano=filtro_ano)

    # Filtro por Avaliação Mínima
    if filtro_avaliacao:
        filmes = filmes.filter(nota__gte=filtro_avaliacao)  # Maior ou igual à nota escolhida
    # --- FIM DO SISTEMA DE FILTROS ---

    # Debug opcional para ver no terminal se os filmes filtrados estão vindo com imagem cadastrada
    for filme in filmes:
        print(f"Filme Filtrado: {filme.titulo} | Foto: {filme.foto}")
    
    # 3. O ÚNICO return render deve ficar aqui no final da função!
    return render(request, 'home.html', {'perfil': perfil, 'filmes': filmes})

def cadastrar(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            perfil = Perfil.objects.create(
                user=user,
                foto=form.cleaned_data['foto']
            )
            
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            link = f"http://localhost:8000/ativar/{uid}/{token}/"
            
            
            print("\n" + "="*50)
            print("COPIE O LINK ABAIXO INTEIRO:")
            print(link)
            print("="*50 + "\n")

            send_mail(
                'Ative sua conta',
                link,
                'web2@ifce.edu.br',
                [user.email]
            )
            
            return render(request, 'cadastro_sucesso.html')
    else:
        form = CadastroForm()
        
    return render(request, 'cadastrar.html', {'form': form})

def ativar_conta(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        perfil = user.perfil
        perfil.email_confirmado = True
        perfil.save()
        return redirect('login')
    else:
        return render(request, 'token_invalido.html')
    
def detalhes_filme(request, filme_id):
    # Busca o filme pelo ID ou mostra página de erro 404 se não achar
    filme = get_object_or_404(Filme, id=filme_id)
    return render(request, 'detalhes.html', {'filme': filme})