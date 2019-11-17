from django.urls import path
from django.contrib import admin
from . import views
urlpatterns = [
    #url(r'^login/', admin.site.urls),
    path('', views.home, name ='home'),
    path('reg/', views.registration),
    path('data/', views.data),
    path('pat/', views.patients),
    path('count/', views.count,name = 'count' ),
    path('about/', views.about,name = 'about' ),
]