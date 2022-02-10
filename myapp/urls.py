from django.urls import path
from myapp import views

urlpatterns = [
    path('myapi/', views.myapi),
    path('update-api/<int:pk>/', views.update_api),
]