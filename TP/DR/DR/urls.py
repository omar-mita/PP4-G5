"""URL configuration for DR project."""
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.index, name='index'),
    path('contacto/', views.contacto, name='contacto'),
    path('loguearse/', views.loguearse, name='loguearse'),
    path('registro/', views.registro, name='registro'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('publicar-perro/', views.publicar_perro, name='publicar_perro'),
    path('cerrar-sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('cambiar-password/', views.cambiar_password, name='cambiar_password'),
    path('mis-publicaciones/', views.mis_publicaciones, name='mis_publicaciones'),
    path('adoptado/<int:animal_id>/', views.marcar_adoptado, name='marcar_adoptado'),
    path('dar-baja/<int:animal_id>/', views.dar_baja_publicacion, name='dar_baja_publicacion'),
    path('editar/<int:animal_id>/', views.editar_publicacion, name='editar_publicacion'),
    path('reportes/', views.reportes, name='reportes'),
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
