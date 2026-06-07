from django.shortcuts import render
from django.contrib import messages


def index(request):
    return render(request, 'index.html')

def permitter_base(request):
    return render(request, 'permitter/permitter_base.html')

def main(request):
    return render(request, 'main.html')

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'admin' and password == 'admin':
            return render(request, 'permitter/permitter_base.html')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'adminlogin.html')

def owner_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'owner' and password == 'owner':
            return render(request, 'index.html')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'ownerlogin.html')