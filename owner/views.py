from django.shortcuts import render, redirect
from .models import CustomUser
from .forms import CustomUserForm
from django.contrib import messages

def register_user(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User registered successfully!')
            return redirect('register')  # redirect to the same page or anywhere
    else:
        form = CustomUserForm()
    return render(request, 'register.html', {'form': form})


def view_users(request):
    data=CustomUser.objects.all()
    return render(request, 'view_users.html', {'data': data})

def activate_user(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    user.status = 'active'
    user.save()
    return redirect('view_users')

def deactivate_user(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    user.status = 'waiting'
    user.save()
    return redirect('view_users')

def delete_user(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    user.delete()
    return redirect('view_users')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try :
            user = CustomUser.objects.get(username=username, password=password)
            if user.status == 'active':
                return render(request, 'crm/base.html')
            else:
                messages.error(request, 'User is not active')
        except CustomUser.DoesNotExist:
            messages.error(request, 'Invalid username or password')
    return render(request, 'userlogin.html')