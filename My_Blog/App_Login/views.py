from django.shortcuts import render
from App_Login.forms import SignUpForm,ProfilePicForm,UserProfileChange
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def sign_up(request):

    sign_up_form = SignUpForm()
  

    if request.method == 'POST':

        sign_up_form = SignUpForm(data=request.POST)

        if sign_up_form.is_valid():

            sign_up_form.save()
            return HttpResponseRedirect(reverse('App_Login:login'))


    dict = {'form' : sign_up_form}
    return render(request, 'App_Login/signup.html', context=dict)

def login_page(request):

    form = AuthenticationForm()

    if request.method == 'POST':

        form = AuthenticationForm(data=request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('App_Blog:blog_list'))



    dict = {'form' : form}
    return render(request, 'App_Login/login.html', context=dict)


@login_required
def display_profile(request):

    dict = {}
    return render(request, 'App_Login/profile.html', context=dict)

@login_required
def change_profile(request):

    form = UserProfileChange(instance=request.user)

    if request.method == 'POST':

        form = UserProfileChange(data=request.POST, instance=request.user)

        if form.is_valid():
            
            form.save(commit=True)
            return HttpResponseRedirect(reverse('App_Login:profile'))




    dict = {'form' : form}
    return render(request, 'App_Login/change_profile.html', context=dict)


@login_required
def change_password(request):

    form = PasswordChangeForm(request.user)

    if request.method == 'POST':

        form = PasswordChangeForm(request.user,request.POST)

        if form.is_valid():

            form.save()
            return HttpResponseRedirect(reverse('App_Login:login'))

    dict = {'form' : form}
    return render(request, 'App_Login/change_password.html', context=dict)


@login_required
def add_profile_pic(request):

    form = ProfilePicForm()


    if request.method == 'POST':

        form = ProfilePicForm(request.POST,request.FILES)

        if form.is_valid():
            form_obj = form.save(commit=False)

            form_obj.user = request.user
            form_obj.save()
            return HttpResponseRedirect(reverse('App_Login:profile'))

    dict = {'form' : form}
    return render(request, 'App_Login/add_profile_pic.html', context=dict)

@login_required
def change_profile_pic(request):

    form = ProfilePicForm(instance=request.user.user_profile)

    if request.method == 'POST':

        form = ProfilePicForm(request.POST,request.FILES, instance=request.user.user_profile)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('App_Login:profile'))

    dict = {'form' : form}
    return render(request, 'App_Login/add_profile_pic.html', context=dict)


@login_required
def logout_page(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_Blog:blog_list'))


 
    

