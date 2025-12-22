from django.urls import path
from . import admin_views  # new file for admin dashboard views

urlpatterns = [
    path('', admin_views.dashboard, name='admin-dashboard'),
    path('products/', admin_views.products_list, name='admin-products'),
    path('products/add/', admin_views.product_add, name='admin-product-add'),
    path('products/<int:pk>/edit/', admin_views.product_edit, name='admin-product-edit'),
    path('products/<int:pk>/delete/', admin_views.product_delete, name='admin-product-delete'),
    path('orders/', admin_views.orders_list, name='admin-orders'),
    path('orders/<int:pk>/', admin_views.order_detail, name='admin-order-detail'),
    path('orders/<int:pk>/delete/', admin_views.order_delete, name='admin-delete-order'),
    path('users/', admin_views.users_list, name='admin-users'),
    path('users/<int:pk>/toggle/', admin_views.user_toggle_active, name='admin-user-toggle'),
    path('users/', admin_views.users_list, name='admin_users'),
    path('users/<int:user_id>/block/', admin_views.admin_toggle_block, name='admin_toggle_block'),
    path('users/<int:user_id>/admin/', admin_views.admin_toggle_admin, name='admin_toggle_admin'),
    path('users/<int:user_id>/superuser/', admin_views.admin_toggle_superuser, name='admin_toggle_superuser'),
    path('users/<int:user_id>/delete/', admin_views.admin_user_delete, name='admin_user_delete'),
    path('categories/', admin_views.categories_list, name='admin-categories'),
    path('categories/<int:pk>/edit/', admin_views.edit_category, name='admin-edit-category'),
    path('categories/add/', admin_views.add_category, name='admin-add-category'),
    path('categories/<int:pk>/delete/', admin_views.delete_category, name='admin-delete-category'),

]
