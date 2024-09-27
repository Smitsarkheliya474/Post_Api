from django.urls import path
from . import views

urlpatterns = [
    path('insert/', views.insert_post, name='insert_post'),   
    path('update/', views.update_post, name='update_post'),
    path('delete/<str:title>/', views.delete_post, name='delete_post'),
    path('view/', views.view_post, name='view_post'),           
]
