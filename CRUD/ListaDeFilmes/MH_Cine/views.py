from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from .forms import CadastroForm
from .models import Perfil
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.decorators import login_required

@login_required 
def home(request):
    perfil = None
    if request.user.is_authenticated:
        # Verifica de forma segura se o usuário tem o objeto perfil
        if hasattr(request.user, 'perfil'):
            perfil = request.user.perfil
        else:
            # Se for um superuser ou usuário sem perfil, podemos criar um ou deixar None
            perfil = None 
            
    # O resto do seu código da view continua igual...
    # Lembre-se de passar o 'perfil' no seu context se o seu HTML precisar dele
    return render(request, 'home.html', {'perfil': perfil})
    if not request.user.perfil.email_confirmado:
        return render(request, 'aguardando_confirmacao.html')
    return render(request, 'home.html')

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
    
