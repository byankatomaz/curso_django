from model_mommy import mommy
from django.test import TestCase
from core.models import get_file_path
import uuid

class GetFilePathTestCase(TestCase):
    
    def setUp(self):
        self.filename = f'{uuid.uuid4()}.png'
        
    def test_get_file_path(self):
        arquivo = get_file_path(None, 'teste.png')

        self.assertTrue(len(arquivo), len(self.filename))
        
        

class ServicoTestCase(TestCase):
    
    def setUp(self):
        self.servico = mommy.make('Servico')
        
    def test_str(self):
        self.assertEquals(str(self.servico), self.servico.servico)  


class CargoTestCase(TestCase):
    
    def setUp(self):
        self.cargo = mommy.make('Cargo')
        
    def test_str(self):
        self.assertEquals(str(self.cargo), self.cargo.cargo)  


class FuncionarioTestCase(TestCase):
    
    def setUp(self):
        self.funcionario = mommy.make('Funcionario')
        
    def test_str(self):
        self.assertEquals(str(self.funcionario), self.funcionario.nome)  
        
class RecursosTestCase(TestCase):
    
    def setUp(self):
        self.recursos = mommy.make('Recursos')
        
    def test_str(self):
        self.assertEquals(str(self.recursos), self.recursos.nome)  
        
        
class PlanosTestCase(TestCase):
    
    def setUp(self):
        self.plano = mommy.make('Planos')
        
    def test_str(self):
        self.assertEquals(str(self.plano), self.plano.plano)  
        
    
class PrecosTestCase(TestCase):
    
    def setUp(self):
        self.preco = mommy.make('Precos')
        
    def test_str(self):
        self.assertEquals(str(self.preco), str(self.preco.preco))  
        
        
class ClienteTestCase(TestCase):
    
    def setUp(self):
        self.cliente = mommy.make('Cliente')
        
    def test_str(self):
        self.assertEquals(str(self.cliente), self.cliente.nome)  