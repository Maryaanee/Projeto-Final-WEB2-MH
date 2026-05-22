from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from .forms import CadastroForm
from .models import Perfil

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
            
            send_mail(
                'Ative sua conta', 
                f'Clique aqui: {link}',
                'web2@ifce.edu.br', 
                [user.email]
            )
            return render(request, 'cadastro_sucesso.html')
    else:
        form = CadastroForm()
        
    return render(request, 'cadastrar.html', {'form': form})