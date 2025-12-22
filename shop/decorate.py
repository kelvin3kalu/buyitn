from django.http import HttpResponseForbidden
# decorate.py
from django.shortcuts import redirect
from django.contrib import messages

def group_required(group_name):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if request.user.groups.filter(name=group_name).exists():
                return view_func(request, *args, **kwargs)
            return HttpResponseForbidden('Access Denied')
        return _wrapped_view
    return decorator


from django.shortcuts import redirect
from django.contrib import messages
from functools import wraps
from .models import Profile

def admin_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("login")

        profile, created = Profile.objects.get_or_create(user=request.user)

        if not profile.is_custom_admin:
            messages.error(request, "Access denied. Admins only.")
            return redirect("product_list")

        return view_func(request, *args, **kwargs)
    return wrapper
