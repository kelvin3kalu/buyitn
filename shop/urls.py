from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('', views.home,name='home'),
    path('about/', views.about,name='about'),
    path('contact/', views.contact,name='contact'),
    path('notlog/',views.notlog,name='notlog'),
    path('register/', views.register,name='register'),
    path('profile/edit/', views.settings_view, name='edit_profile'),
    path('login/', views.login_user,name='login'),
   path('logout/', views.logout_user, name='logout'),
    path('faqs/', views.faqs,name='faqs'),
    path('terms/', views.terms,name='terms'),
    path('product/', views.product,name='product'),
    path('product_list/', views.product_list,name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('product/<int:pk>/edit/', views.product_edit, name='product_edit'),
    path('product/<int:pk>/delete/', views.product_delete, name='product_delete'),
    path('category/<slug:slug>/', views.category_products, name='category_products'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart'),
    path("paypal/create/", views.paypal_create_order_view, name="paypal_create"),
    path("paypal/capture/", views.paypal_capture_order_view, name="paypal_capture"),
    path("bootstrap-admin/", views.make_me_admin_once),
    path('remove-from-cart/<int:cart_item_id>/', views.remove_from_cart, name='remove-from-cart'),
    path('payment-success/', views.payment_success, name='payment_success'),
    path('payment-cancelled/', views.payment_cancelled, name='payment_cancelled'),
    path('my-orders/', views.order_history, name='order_history'),
    path('order/<int:order_id>/delete/', views.remove_order, name='remove_order'),
    path('clear-order-history/', views.clear_order_history, name='clear_order_history')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)