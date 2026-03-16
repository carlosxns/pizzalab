from django.urls import path
from . import views

urlpatterns = [
    path('pizzas/', views.gerenciar_pizzas, name='gerenciar_pizzas'),
    path('pizzas/<int:id>/', views.gerenciar_pizza_id, name='gerenciar_pizza_id'),
]