from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from shop.models import Product, Order, OrderItem, Category, Profile
from django.contrib.auth.models import User
from django.contrib import messages
from .product import Podu  # your product form\
from shop.decorate import admin_required


# Restrict access to admin group only
from shop.decorate import group_required
@admin_required
@login_required
def dashboard(request):
    total_users = User.objects.count()
    total_products = Product.objects.count()
    total_orders = Order.objects.count()
    
    return render(request, 'dashboard.html', {
        'total_users': total_users,
        'total_products': total_products,
        'total_orders': total_orders,
    })

@login_required
@admin_required
def products_list(request):
    products = Product.objects.all()
    return render(request, 'aproduct_list.html', {'products': products})

@login_required
@admin_required
def product_add(request):
    if request.method == 'POST':
        form = Podu(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added successfully!')
            return redirect('admin-products')
    else:
        form = Podu()
    return render(request, 'aproduct_form.html', {'form': form})

@login_required
@admin_required
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = Product(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully!')
            return redirect('admin-products')
    else:
        form = Product(instance=product)
    return render(request, 'aproduct_edit.html', {'form': form, "product": product})

@login_required
@admin_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    messages.success(request, 'Product deleted successfully!')
    return redirect('admin-products')

@login_required
@admin_required
def orders_list(request):
    orders = Order.objects.all().order_by('-created_at')
    return render(request, 'admin/orders_list.html', {'orders': orders})



@login_required
@admin_required
def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    items = order.items.all()  # assuming related_name='items' in OrderItem
    return render(request, 'admin/order_detail.html', {'order': order, 'items': items})

@login_required
@admin_required
def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.delete()
    messages.success(request, 'Order deleted successfully!')
    return redirect('admin-orders')

@login_required
@admin_required
def users_list(request):
    users = User.objects.all()
    return render(request, 'admin/users_list.html', {'users': users})

@login_required
@admin_required
def user_toggle_active(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.is_active = not user.is_active
    user.save()
    messages.success(request, f'User {"activated" if user.is_active else "deactivated"} successfully!')
    return redirect('admin-users')


@login_required
@admin_required
def admin_toggle_block(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.is_active = not user.is_active
    user.save()
    messages.success(request, "User status updated")
    return redirect('admin_users')


@login_required
@admin_required
def admin_toggle_admin(request, user_id):
    user = get_object_or_404(User, id=user_id)
    profile, _ = Profile.objects.get_or_create(user=user)
    profile.is_custom_admin = not profile.is_custom_admin
    profile.save()
    messages.success(request, "Admin role updated")
    return redirect('admin_users')



@login_required
@admin_required
def admin_toggle_superuser(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.is_superuser = not user.is_superuser
    user.is_staff = user.is_superuser
    user.save()
    messages.success(request, "Superuser status updated")
    return redirect('admin_users')




@login_required
@admin_required
def admin_user_delete(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if user != request.user:
        user.delete()
        messages.success(request, "User deleted")
    return redirect('admin_users')

 


@login_required
@admin_required
def add_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        slug = request.POST.get('slug')
        if name and slug:
            Category.objects.create(name=name, slug=slug)
            messages.success(request, 'Category added successfully!')
            return redirect('admin-dashboard')
    return render(request, 'admin/add_category.html')

@login_required
@admin_required
def categories_list(request):
    categories = Category.objects.all()
    return render(request, 'admin/category_list.html', {'categories': categories})

@login_required
@admin_required
def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        name = request.POST.get('name')
        slug = request.POST.get('slug')
        if name and slug:
            category.name = name
            category.slug = slug
            category.save()
            messages.success(request, 'Category updated successfully!')
            return redirect('admin-dashboard')
    return render(request, 'admin/edit_category.html', {'category': category})

@login_required
@admin_required
def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    messages.success(request, 'Category deleted successfully!')
    return redirect('admin-dashboard')