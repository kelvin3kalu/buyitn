# shop/decorate.py
from django.shortcuts import redirect
from django.contrib import messages
from functools import wraps
from .models import Profile

def admin_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("login")

        profile, _ = Profile.objects.get_or_create(user=request.user)

        # ✅ allow first-ever admin
        if not Profile.objects.filter(is_custom_admin=True).exists():
            profile.is_custom_admin = True
            profile.save()
            return view_func(request, *args, **kwargs)

        # 🔒 normal admin check
        if not profile.is_custom_admin:
            messages.error(request, "Admins only.")
            return redirect("product_list")

        return view_func(request, *args, **kwargs)

    return wrapper
