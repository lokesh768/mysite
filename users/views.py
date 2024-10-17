from django.shortcuts import render, redirect
from .forms import RegisterForm, EditProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile



def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Welcome {username}, your account is registered successfully')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form':form})

@login_required()
def profilepage(request):
    return render(request, 'users/profile.html')

@login_required()
def editprofile(request):
    if request.method == "POST":
        profile, created = Profile.objects.get_or_create(user=request.user)
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile edited Successfully')
            return redirect('profile')
    else:
        form = EditProfileForm()
    
    return render(request, 'users/editprofile.html', {'form': form})

