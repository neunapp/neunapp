"""swn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
#from django.views.generic.base import RedirectView
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #urls para aplicacion blog
    url(r'^', include('applications.home.urls', namespace='home_app')),
    #url para aplicicon cotizacion
    url(r'^', include('applications.cotizacion.urls', namespace='cotizacion_app')),
    #url para aplicacion productos
    url(r'^', include('applications.productos.urls', namespace='productos_app')),
    #url para aplicacion blog
    url(r'^', include('applications.blog.urls', namespace="blog_app")),

    #url para editor de texto
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
