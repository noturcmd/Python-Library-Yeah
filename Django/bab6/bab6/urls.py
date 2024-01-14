from django.contrib import admin
from django.urls import path
from . import views
from myprofile import views as profilViews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('profil/', profilViews.index),
    path('', views.index),
    path('index', views.index),
]
