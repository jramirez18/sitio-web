from django.conf.urls import include, url, patterns
from . import views

urlpatterns = patterns('',
    url(r'^$', views.listar_publicaciones),
    url(r'^login/$',views.ingresar, name='ingresar'),
    url(r'^close/$', views.salir, name='salir'),
    url(r'^about/$', views.about, name='about'),
    url (r'^post/(?P<pk>[0-9]+)/$', views.detalle_publicacion),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.editar_publicacion, name='editar_publicacion'),
    url(r'^post/new/$', views.nueva_publicacion, name='nueva_publicacion'),
    url(r'^post/(?P<pk>[0-9]+)/delete/$', views.eliminar_publicacion, name='eliminar_publicacion'),

)