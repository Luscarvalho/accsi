from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    @staticmethod
    def process_view(request, view_func, view_args, view_kwargs):
        # Verifica se a view é baseada em classe
        if hasattr(view_func, 'view_class'):
            view_class = view_func.view_class
            # Aplica o decorador login_required se a view é baseada em classe
            if not getattr(view_class, 'skip_login_required', False):
                view_func = method_decorator(login_required)(view_func)
        else:
            # Aplica o decorador login_required se a view é uma função
            if not getattr(view_func, 'skip_login_required', False):
                view_func = login_required(view_func)

        # Chama a função decorada com o objeto request
        return view_func(request, *view_args, **view_kwargs)

