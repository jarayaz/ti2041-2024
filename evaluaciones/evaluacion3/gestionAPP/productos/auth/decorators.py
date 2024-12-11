from django.contrib.auth.decorators import user_passes_test
from functools import wraps

def admin_products_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.session.get('is_admin_products'):
            return redirect('login')
        return view_func(request, *args, **kwargs)
    return _wrapped_view
