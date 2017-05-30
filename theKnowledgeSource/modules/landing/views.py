from django.shortcuts import render,redirect
from .forms import SignupForm,LoginForm
from django.contrib.auth.models import User
from modules.users.models import User
from django.contrib.auth import authenticate,logout as salir,login as iniciar
from django.http import HttpResponse

# Create your views here.
def index(request):
    form_login = LoginForm(request.POST or None)
    form_sign = SignupForm(request.POST or None)
    return render(request,'landing/index.html',{'login':form_login, 'sign':form_sign})


def login(request):
    form = LoginForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = authenticate(
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
                )
            if user is not None:
                iniciar(request,user)
                return redirect('landing:index')
            else:
                return redirect('landing:index')#usuario no registrado

    return render(request,'landing/index.html')



def signup(request):
    form = SignupForm(request.POST or None)
    if request.method == 'POST':
        print(form.is_valid())
        if form.is_valid():
            form.cleaned_data.pop('confirm_password', None)
            user = User.objects.create_user(**form.cleaned_data)
            if user is not None:
                iniciar(request,user)    
                return redirect("landing:index")
                
    return render(request,'landing/index.html')
            
    


def logout(request):
    salir(request)
    return redirect("landing:index")
