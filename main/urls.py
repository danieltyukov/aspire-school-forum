from django.urls import path
from . import views

urlpatterns = [
    path('register', views.registerPage, name='register'),
    path('', views.homePage, name='index'),
    path('question/<int:id>', views.questionPage, name='question')
]
