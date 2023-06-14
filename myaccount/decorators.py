from django.shortcuts import redirect
from django.urls import reverse


def user_not_authenticated(function=None):
    """
    Decorator for views that checks that the user is NOT logged in, redirecting to
    the registration page if necessary, and to the user_info page if authenticated.
    """
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated:
                user_id = request.user.id
                return redirect(reverse('user_info', args=[user_id]))
            else:
                return redirect('user_register')

        return _wrapped_view

    if function:
        return decorator(function)

    return decorator
