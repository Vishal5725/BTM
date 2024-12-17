from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home_page_redirect, name='home'),  # Add a redirect view for the home page
    path('register-admin/', register_admin, name='register_admin'),  # Ensure this path is for registration
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('add-product/', add_product, name='add_product'),
    path('delete-product/<int:product_id>/', delete_product, name='delete_product'),
    path('login/', custom_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
