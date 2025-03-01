from django.urls import path
from app1.views import hola_mundo,chaooooo
from django.urls import path,include
urlpatterns = [
    path('',hola_mundo),
    path('app1',chaooooo.as_view()),
]





