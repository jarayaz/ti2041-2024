from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            # Guardar datos en sesión
            request.session['user_name'] = user.username
            request.session['login_date'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            request.session['is_admin_products'] = user.groups.filter(name='ADMIN_PRODUCTS').exists()
            return redirect('consulta_productos')
        else:
            return render(request, 'login.html', {'error': 'Usuario o contraseña incorrectos'})
            
    return render(request, 'login.html')
