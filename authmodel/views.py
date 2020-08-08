from django.shortcuts import render, HttpResponseRedirect, redirect, HttpResponse
from .forms import SignupForm, UserForm, LoginForm, SetPassword, AdminForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm, UserChangeForm, User
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash



def sign_up(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'sucessfully create account')
            form = SignupForm()
            return HttpResponseRedirect('/login/')
        else:
            messages.error(request, 'Form is Not Valid')
    else:
        form = SignupForm()

    context = {'form': form}
    return render(request, 'signup.html', context)


def login_(request):
    if not request.user.is_authenticated:

        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                users = authenticate(username=username, password=password)
                if users is not None:
                    login(request, users)
                    return HttpResponseRedirect('/profile/')
                else:
                    messages.error(request, 'something went to wrong')
            else:
                messages.error(
                    request, 'Please Enter Correct Detail or Check Password or User Name')
        else:
            form = LoginForm()
    else:
        return HttpResponseRedirect('/profile/')

    context = {'form': form}
    return render(request, 'login.html', context)


def profile_page(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            userinfo = User.objects.all()
            user = request.user
        else:
            user = request.user
            userinfo = None

    else:
        messages.error(request, 'please First login')
        return HttpResponseRedirect('/login/')
    context = {'user': user, 'userinfo':userinfo}
    return render(request, 'profile.html', context)


def log_out(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/login/')

    else:
        messages.error(request, 'First login')
        return HttpResponseRedirect('/login/')


def change_password(request):
    if request.user.is_authenticated:
        if request.method == "POST":

            form = SetPassword(user=request.user, data=request.POST)
            print('ok0')
            if form.is_valid():
                form.save()
                print('okok')
                messages.success(request, 'password change successfully')
                update_session_auth_hash(request, form.user)
                return HttpResponseRedirect('/profile/')
        else:
            form = SetPassword(user=request.user)
    else:
        messages.error(request, 'Login First')
        return HttpResponseRedirect('/login/')

    context = {'form': form}
    return render(request, 'changepassword.html', context)


def change_profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            user = request.user
            if request.user.is_superuser:
                form = AdminForm(request.POST, instance=request.user)
            else:   
                form = UserForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, 'profile change successfully')
                return HttpResponseRedirect('/profile/')
            else:
                messages.error(request, 'some mistack')
                return HttpResponseRedirect('/changeprofile/')

        else:
            if request.user.is_superuser:
                form = AdminForm(instance=request.user)
            else:
                form = UserForm(instance=request.user)
            context = {'form': form}
            return render(request, 'change_profile.html', context)
    else:
        messages.error(request, 'Login First')
        return HttpResponseRedirect('/login/')

def userdetail(request, id):
    if request.user.is_superuser:
        user = User.objects.get(pk=id)
        form = AdminForm(instance=user)
    else:
        return HttpResponse('You Are Not Authorized User ')
    context = {'form':form}
    return render(request, 'userdetail.html', context)