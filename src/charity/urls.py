"""charity URL Configuration

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
from django.conf.urls.static import static
from django.conf import settings

from .views import index, gallery, about_us, activities, contact, donate, projects, sponser, sponsor_a_child

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('gallery/', gallery),
    path('about-us/', about_us),
    path('activities/', activities),
    path('contact/', contact),
    path('donate/', donate),
    path('projects/', projects),
    path('sponser/', sponser),
    path('sponsor-a-child/', sponsor_a_child),
    
]
if settings.DEBUG:
    urlpatterns  += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns  += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
