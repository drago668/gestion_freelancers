"""
URL configuration for gestion_freelancers project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from gestion.views import index, contrato, proyecto,tiempo, perfil,registrar,proyectos,actualizar_estado_proyecto,gestion_contratos,editar_contrato,eliminar_contrato,editar_proyecto,eliminar_proyecto
from django.contrib.auth import views as auth_views
from gestion import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path("", index, name='inicio'),
    path('contrato/', contrato, name='contrato'),
    path('proyecto/', proyecto,name='proyecto'),
    path('tiempo/', tiempo, name='tiempo'),
    path('perfil/', perfil, name='perfil'),
    path('registrar/', registrar, name='registrar'),
    #path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    #path('login/', LoginView.as_view(), name='login'),
    path("proyectos/", proyectos, name="proyectos"),
    path("proyectos/editar_estado/<int:proyecto_id>/", actualizar_estado_proyecto, name="editar_estado_proyecto"),
    path("gestion_contratos/", gestion_contratos, name="gestion_contratos"),
    path('contrato/editar/<int:contrato_id>/', editar_contrato, name='editar_contrato'),
    path('contrato/eliminar/<int:contrato_id>/', eliminar_contrato, name='eliminar_contrato'),
    path('proyecto/eliminar/<int:proyecto_id>/', eliminar_proyecto, name='eliminar_proyecto'),
    path('tareas/', views.seguimiento_tareas, name='seguimiento_tareas'),
    path('tarea/<int:id_tarea>/', views.detalle_tarea, name='detalle_tarea'),
    path('tarea/<int:tarea_id>/iniciar/', views.iniciar_seguimiento, name='iniciar_seguimiento'),
    path('seguimiento/<int:seguimiento_id>/detener/', views.detener_seguimiento, name='detener_seguimiento'),
    path('tarea/<int:tarea_id>/resetear/', views.resetear_seguimiento, name='resetear_seguimiento'),
    path('proyecto/editar/<int:proyecto_id>/', editar_proyecto, name='editar_proyecto'),
    path('proyecto/<int:proyecto_id>/crear_tarea/', views.crear_tarea, name='crear_tarea'),


     
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
