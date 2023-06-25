from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
     path('admin/', admin.site.urls),
    # path('', include('coreapp.urls')),
    path('',views.signup), 
    path('H1',views.lastpage),
    path('home',views.Home),
    path('subcategeory',views.subcategeory),
    path('login',views.login),
    path('home',views.Home1),
]