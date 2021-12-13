"""examen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from encuesta import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('agregar-encuesta/', views.agregar_encuesta, name='agregar_encuesta'),
    path('agregar-interes-personal/<int:pk>/', views.agregar_interes, name='agregar_interes'),
    path('reporte-encuesta-pdf/<int:pk>/', views.ReporteEncuestaPDF.as_view(), name='ReporteEncuestaPDF'),
    path('editar-interes-personal/<int:id_i>/<int:pk>/', views.editar_interes, name='editar_interes'),
    path('eliminar-interes-personal/<int:id_i>/<int:pk>/', views.eliminar_interes, name='eliminar_interes'),
    path('mis-intereses/<int:pk>/', views.mis_intereses, name='mis_intereses')
]
