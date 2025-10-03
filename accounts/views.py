from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, AuthenticationForm, UserChangeForm
from django.contrib.auth import update_session_auth_hash, authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.forms import ProfileForm

def register_view(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('login')
    else:
        user_form = UserCreationForm()
    return render(request, 'register.html', {'user_form': user_form})

@login_required
def change_view(request):
    if request.method == 'POST':
        change_form = PasswordChangeForm(user=request.user, data=request.POST)
        if change_form.is_valid():
            user = change_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Senha alterada com sucesso!')
            return redirect('login')
    else:
        change_form = PasswordChangeForm(user=request.user)
    return render(request, 'change.html', {'change_form': change_form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('cars_list')
        else:
            login_form = AuthenticationForm()
    else:
        login_form = AuthenticationForm()
    return render(request, 'login.html', {'login_form': login_form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('cars_list')

@login_required
def profile_view(request):
    return render(request, 'profile.html', {"user": request.user})

@login_required
def edit_profile_view(request):
	if request.method =='POST':
		profile_form = ProfileForm(request.POST, request.FILES)
		if profile_form.is_valid():
			profile_form.save()
			return redirect('cars_list')
	else:
		profile_form = ProfileForm()
	return render(request, 'editprofile.html', {'profile_form': profile_form})
