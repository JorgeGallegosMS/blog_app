from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('blog-index')
    else:
        form = RegisterForm(request.POST)

    return render(request, 'users/register.html', {'form': form })