from django.urls import path

from . import views

app_name = 'f5day'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:activity_id>/register', views.register, name='register')
]