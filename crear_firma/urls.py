from django.urls import path
from crear_firma import views



urlpatterns = [
    path('', views.index, name='home'),
    path('/firma', views.crear_firma, name='firma')
]