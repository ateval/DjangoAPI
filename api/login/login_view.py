from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.filter(email=email).first()
        if user:
            user = authenticate(username=user.username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        messages.error(request, 'Correo electrónico o contraseña incorrectos.')
    return render(request, 'login.html')


def register_view(request):
    template_name = "register.html"

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        terms = request.POST.get('terms')  # Obtener el checkbox de términos

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Usuario ya existe')
            return render(request, template_name)
    
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Ya hay una cuenta con este correo electrónico.')
            return render(request, template_name)
        
        if password != confirm_password:
            messages.error(request, 'Las contraseñas no coinciden.')
            return render(request, template_name)

        # Verificar que el usuario ha aceptado los términos y condiciones
        if not terms:
            messages.error(request, 'Debes aceptar los términos y condiciones.')
            return render(request, template_name)

        try:
            user = User(
                username=username,
                email=email,
                password=make_password(password),  # Hashear la contraseña
            )
            user.save()
            messages.success(request, '¡Registro exitoso! Ahora puedes iniciar sesión.')
            return redirect('login') 
        except Exception as e:
            messages.error(request, f'Error al registrar el usuario: {e}')
            return render(request, template_name)
        
    return render(request, template_name)
