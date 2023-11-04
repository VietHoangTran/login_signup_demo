from django.urls import path, include
from api import views

urlpatterns = [
    path('signup/', views.signup),
    path('login/', views.login),
    path('test_token/', views.test_token),
]