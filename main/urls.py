from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='index'),
    path('question/<int:id>',views.questionPage, name='question')
]
