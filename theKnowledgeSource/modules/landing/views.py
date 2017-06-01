from django.shortcuts import render,redirect
from .forms import SignupForm,LoginForm
from django.contrib.auth.models import User
from modules.users.models import User
from django.contrib.auth import authenticate,logout as salir,login as iniciar
from django.http import HttpResponse
from modules.playlists.forms import PlaylistForm
from modules.recursos.forms import RecursoForm

# Create your views here.
def index(request):
    form_login = LoginForm(request.POST or None)
    form_sign = SignupForm(request.POST or None)
    form_playlist = PlaylistForm(request.POST or None)
    form_recurso = RecursoForm(request.POST or None)

    return render(request,'landing/index.html',{'login':form_login, 'sign':form_sign,
        'playlist':form_playlist,
        'recurso': form_recurso,
        
        }
    )


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


def add_playlist(request):
    if request.method == 'POST':
        form_playlist = PlaylistForm(request.POST or None)
        print(form_playlist)
        if form_playlist.is_valid():
            Playlist = form_playlist.save(commit=False)
            u = request.user
            Playlist.user = u
            Playlist.save()
            return redirect('landing:index')
        else:
            return HttpResponse('hola')
    
        

def add_recurso(request):
       if request.method == 'POST':
           form_recurso = RecursoForm(request.POST)
           if form_recurso.is_valid():
                Recurso = form_recurso.save(commit=False)
                u = request.user
                Recurso.user = u
                Recurso.save()
                return redirect('landing:index')