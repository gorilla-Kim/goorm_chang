from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="board_main"),
    path('new/', views.create_board, name="create_board"),
    path('read/<int:pk>', views.read_board, name="read_board"),
]
