from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            print('form saved')
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created. Now you can login. {username}!')
            return redirect('login')
        else:
            messages.error(request, f'Your form is invalid!')

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})


def profile(request):
    return render(request, 'users/profile.html')


