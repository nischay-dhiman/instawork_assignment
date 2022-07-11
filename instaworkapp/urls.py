from django.urls import path
from instaworkapp import views

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'create/', views.create, name='create'),
    path(r'update/<int:mem_id>', views.update, name='update'),
    path(r'delete/<int:mem_id>', views.delete, name='delete'),
]
