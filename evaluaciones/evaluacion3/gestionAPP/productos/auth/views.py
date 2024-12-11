from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from datetime import datetime

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            request.session['user_name'] = user.username
            request.session['login_date'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            request.session['is_admin_products'] = user.groups.filter(name='ADMIN_PRODUCTS').exists()
            return redirect('consulta_productos')
            
    return render(request, 'auth/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
