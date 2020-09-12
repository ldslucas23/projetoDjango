from django.urls import path
from . import views

urlpatterns = [
    #O endereço /helloworld vai cair em uma view
    path('helloworld/', views.helloWorld),
]