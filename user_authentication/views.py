from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages

# modules needed for user authentication
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

#for pasword reset
from django.contrib.auth import views

# importing the use model
from django.contrib.auth import get_user_model
User = get_user_model()


# importing the forms
from .forms import LoginForm, RegisterForm

# Create your views here.

def home(request):
    return render(request, 'index.html',)



# routes for user registration
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            # form.save only works when form is created from a model
            form.save()
            messages.success(request, 'succesfully created account')
            return redirect('login')
        else:
            # rendering the template again if the form is not valid with the prepopulated data.
            return render(request, 'register.html', {'form': form})

    else:
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})


def login_user(request):
    # redirect user to home if already logged in
    if request.user.is_authenticated:
        messages.info(request, 'You Are Already Logged In')
        return redirect('/home')

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            username = User.objects.filter(email = form.cleaned_data.get('email')).first()
            # the authenticate function returns the user object if the user is found else it returns none
            user = authenticate(username=username, password=form.cleaned_data.get('password'))
            if user:
                login(request, user)
                messages.success(request, 
                f'successfully logged in as {user.username}')
                return redirect('/home')
            else:
                messages.error(request, 'Invalid credentials')
                # form.add_error('user not found')
                return redirect('/login')

        # if form is not valid render the template again with pre populated data
        else:
            return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


@login_required
def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        messages.info(request, 'successfully logged out')
        return redirect('/home')



def change_password(request):
    template_response = views.password_change(request)
    return template_response