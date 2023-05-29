from django.urls import path

from HOMEWORK_16.tms.todos import views

urlpatterns = [
    path('/', views.home, name="home"),
    path('/api', views.posts),
    ]