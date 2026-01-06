# decorate.py
from django.shortcuts import redirect
from django.contrib import messages
from functools import wraps

def admin_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, "Please log in first.")
            return redirect("login")

        if not hasattr(request.user, 'profile') or not request.user.profile.is_custom_admin:
            messages.error(request, "Admin access only.")
            return redirect("product_list")

        return view_func(request, *args, **kwargs)
    return wrapper
