from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('futbol/', views.futbol, name='futbol'),
    path('baloncesto/', views.baloncesto, name='baloncesto'),
    path('tenis/', views.tenis, name='tenis'),
    path('natacion/', views.natacion, name='natacion'),
]