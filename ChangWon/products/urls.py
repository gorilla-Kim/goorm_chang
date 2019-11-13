from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="productsList"),
    path('order/', views.order, name="order"),
    path('<int:pk>/', views.product_view, name='product_view'),
]
