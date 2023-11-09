from django.test import TestCase, Client
from django.urls import reverse_lazy

class IndexViewTestCase(TestCase):
    
    def setUp(self):
        
         self.dados = {
            'nome': 'Samuel Monteiro',
            'email': 'samuel@gmail.com',
            'assunto': 'Um assunto ai',
            'mensagem': 'Uma mensagem qualquer',
        }
         
         self.cliente = Client()
    
    def test_form_valid(self):
        request = self.cliente.post(reverse_lazy('index'), data=self.dados)
        self.assertEquals(request.status_code, 302)
    
    def test_form_invalid(self):
        
        dados = {
            'nome': 'Samuel Monteiro',
            'assunto': 'Um assunto ai',
        }
        
        request = self.cliente.post(reverse_lazy('index'), data=dados)
        self.assertEquals(request.status_code, 200)
        