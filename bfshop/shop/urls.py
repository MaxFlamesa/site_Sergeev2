from django.urls import path
from . import views
from django.conf.urls import include

urlpatterns = [
    path('', views.index, name = 'index'),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),
    path('cart/', include('cart_manager.urls')),
]