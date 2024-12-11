from django.core.exceptions import PermissionDenied

def check_session_admin_products(request):
    """Utility function to check if user has admin products permission in session"""
    if not request.session.get('is_admin_products'):
        raise PermissionDenied("No tienes permisos para realizar esta acción")
