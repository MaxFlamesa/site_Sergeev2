from django.urls import path
from . import views
from django.conf.urls import include

urlpatterns = [
    path('', views.index, name = 'index'),
    path('login/', views.login_page, name = 'login_page'),
    path('cart/', include('cart_manager.urls')),
]