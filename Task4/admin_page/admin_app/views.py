from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import user_passes_test,login_required
from .models import *
from .form import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

def home_page_redirect(request):
    if request.user.is_authenticated:
        # If the user is logged in, redirect to the admin dashboard
        return redirect('admin_dashboard')
    else:
        # If the user is not logged in, redirect to the registration page
        return redirect('register_admin')
    
# Register admin view (only accessible to unauthenticated users)
def register_admin(request):
    if request.user.is_authenticated:
        return redirect('admin_dashboard')  # If the user is logged in, redirect to the dashboard
    if request.method == 'POST':
        form = AdminRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New admin user registered successfully.')
            return redirect('login')  # Redirect to the login page after successful registration
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = AdminRegistrationForm()
    context = {
        'form': form,
        'page_title': 'Register New Admin',
    }
    return render(request, 'register_admin.html', context)

def custom_login(request):
    if request.method == 'POST':
        form = CustomLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('admin_dashboard')  # Redirect to the admin dashboard after login
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = CustomLoginForm()
    return render(request, 'admin_login.html', {'form': form})

# Product Add Form View
@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.uploaded_by = request.user  # Assign the logged-in user as the uploader
            product.save()
            return redirect('admin_dashboard')  # Redirect to the admin dashboard after saving
    else:
        form = ProductForm()

    context = {
        'page_title': 'Add Product',
        'form': form,
    }
    return render(request, 'product.html', context)

@staff_member_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id, uploaded_by=request.user)  # Ensure only the uploader can delete
    product.delete()
    return redirect('admin_dashboard')

# Admin Dashboard View
@login_required
def admin_dashboard(request):
    # Get products uploaded by the logged-in user
    products = Product.objects.filter(uploaded_by=request.user)
    
    context = {
        'page_title': 'Your Products',  # Title for the page
        'products': products,  # Pass the filtered products
    }
    return render(request, 'admin_dashboard.html', context)