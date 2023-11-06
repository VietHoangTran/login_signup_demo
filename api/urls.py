from django.urls import path, include
from api import views

urlpatterns = [
    path('signup/', views.signup),
    path('login/', views.login),
    path('logout/', views.logout_user),
    path('get_info/', views.get_info),
]