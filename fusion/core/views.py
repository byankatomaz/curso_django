from django.http import HttpResponse
from django.views.generic import TemplateView, FormView
from .models import Servico, Funcionario, Recursos, Precos, Cliente
from .forms import ContatoForm
from django.urls import reverse_lazy
from django.contrib import messages


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        
        context['servicos'] = Servico.objects.all()
        context['funcionarios'] = Funcionario.objects.all() 
        context['recursos'] = Recursos.objects.all()
        context['precos'] = Precos.objects.all()
        context['cliente'] = Cliente.objects.all()
        
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso')
        
        return super(IndexView, self).form_valid(form, *args, **kwargs)
    
    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar o E-mail')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)
    
    
