from ninja.errors import HttpError

def require_role(roles):
    def decorator(func):
        def wrapper(request, *args, **kwargs):
            if request.user_role not in roles:
                raise HttpError(403, "Forbidden")
            return func(request, *args, **kwargs)
        return wrapper
    return decorator
