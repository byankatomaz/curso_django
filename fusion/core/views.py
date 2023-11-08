from django.views.generic import TemplateView
from .models import Servico, Funcionario, Recursos


class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        
        context['servicos'] = Servico.objects.all()
        context['funcionarios'] = Funcionario.objects.all() 
        context['recursos'] = Recursos.objects.all()
        
        return context
    
