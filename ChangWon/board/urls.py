from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="board_main"),
    path('new/', views.create_board, name="create_board"),
    path('read/<int:pk>', views.read_board, name="read_board"),
    path('update_board/<int:pk>', views.update_board, name="update_board"),
    path('updatepage/<int:pk>', views.updatepage, name="updatepage"),
    path('delete_board/<int:pk>', views.delete_board, name="delete_board"),
]
