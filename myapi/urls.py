from django.urls import path
from . import views

urlpatterns = [
    path('', views.getAll),
    path('sum', views.getSum, name='sum'),
    path('buy/<int:id>/', views.buyOne, name='buy')
     ]
