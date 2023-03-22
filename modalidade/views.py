from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from .models import Modalidade


@method_decorator(login_required, name='dispatch')
class ListarModalidade(ListView):
    template_name = 'listar_modalidade.html'
    model = Modalidade
    context_object_name = 'modalidades'
