from django.shortcuts import render, get_object_or_404 #ERROR QUE DAN LAS PAGINAS WEB CUANDO INTENTAMOS ENTRAR A UNA PAG Q NO EXISTE
from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from .models import Instrumento
from .forms import PostForm

# Create your views here.
def listar_publicaciones(request):
    publicacion= Instrumento.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'principal/index.html', {'publicacion':publicacion})

def detalle_publicacion(request, pk):
    post = get_object_or_404(Instrumento, pk=pk)
    return render(request, 'principal/detalle_publicacion.html', {'post': post})

def editar_publicacion(request, pk):
        post = get_object_or_404(Instrumento, pk=pk)
        if request.method == "POST":
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                #post.nombre = request.user
                post.save()
                return redirect('principal.views.detalle_publicacion', pk=post.pk)
        else:
            form = PostForm(instance=post)
        return render(request, 'principal/editar_publicacion.html', {'form': form})

def nueva_publicacion(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            #post.autor = request.user
            post.save()
            return redirect('principal.views.detalle_publicacion', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'principal/nueva_publicacion.html', {'form': form})


def eliminar_publicacion(request, pk):
    note = get_object_or_404(Instrumento, pk=pk).delete()
    return redirect('principal.views.listar_publicaciones')