from django.shortcuts import render, render_to_response, get_object_or_404 #ERROR QUE DAN LAS PAGINAS WEB CUANDO INTENTAMOS ENTRAR A UNA PAG Q NO EXISTE
from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from .models import Instrumento
from .forms import PostForm
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.
def listar_publicaciones(request):
    publicacion= Instrumento.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'principal/index.html', {'publicacion':publicacion})

def about(request):
	return render(request, 'principal/about.html')

def detalle_publicacion(request, pk):
    post = get_object_or_404(Instrumento, pk=pk)
    return render(request, 'principal/detalle_publicacion.html', {'post': post})

@login_required(login_url='/login')
def editar_publicacion(request, pk):
        post = get_object_or_404(Instrumento, pk=pk)
        if request.method == "POST":
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.autor = request.user
                post.save()
                return redirect('principal.views.detalle_publicacion', pk=post.pk)
        else:
            form = PostForm(instance=post)
        return render(request, 'principal/editar_publicacion.html', {'form': form})

@login_required(login_url='/login')
def nueva_publicacion(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('principal.views.detalle_publicacion', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'principal/nueva_publicacion.html', {'form': form})
    

@login_required(login_url='/login')
def eliminar_publicacion(request, pk):
    note = get_object_or_404(Instrumento, pk=pk).delete()
    return render(request, 'principal/eliminar_publicacion.html')


def ingresar(request):
    #if not request.user.is_anonymous():
     #   return HttpResponseRedirect('/')
    if request.method == "POST":
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario,password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    return HttpResponseRedirect('/')
                else:
                    return render(request, 'principal/user_no_activo.html')
            else:
                return render(request, 'principal/not_user.html')
    else:
        formulario = AuthenticationForm()
        return render(request,'principal/login.html', {'formulario': formulario})


@login_required(login_url='/')
def salir(request):
    logout(request)
    return HttpResponseRedirect('/')
