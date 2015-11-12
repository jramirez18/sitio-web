from django.shortcuts import render, get_object_or_404 #ERROR QUE DAN LAS PAGINAS WEB CUANDO INTENTAMOS ENTRAR A UNA PAG Q NO EXISTE
from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from .models import Instrumento

# Create your views here.
def listar_publicaciones(request):
    publicacion= Instrumento.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'principal/index.html', {'publicacion':publicacion})

def detalle_publicacion(request, pk):
    post = get_object_or_404(Instrumento, pk=pk)
    return render(request, 'principal/detalle_publicacion.html', {'post': post})