from django.db import models
from stdimage.models import StdImageField
import uuid

def get_file_path(_instace, filename):
    ext = filename.split('.', -1)
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)
    
    class Meta:
        abstract = True


class Servico(Base):
    ICONE_CHOICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Grafico'),
        ('lni-users', 'Usuários'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
    )
    
    servico = models.CharField('Serviço', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Icone', max_length=12, choices=ICONE_CHOICES)
    
    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'
    
    def __str__(self):
        return self.servico
    

class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=100)
    
    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'
        
    def __str__(self) -> str:
        return self.cargo


class Funcionario(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey('core.cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=200)
    imagem = StdImageField('Imagem', upload_to='equipe', variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')
    
    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'
        
    def __str__(self) -> str:
        return self.nome


class Recursos(Base):
    ICONE_CHOICES = (
        ('lni-rocket', 'Foguete'),
        ('lni-laptop-phone', 'Computador/Celular'),
        ('lni-cog', 'Engrenagem'),
        ('lni-leaf', 'Folha'),
        ('lni-layers', 'Design'),
    )
    
    nome = models.CharField('Recurso', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Icone', max_length=16, choices=ICONE_CHOICES)
    
    class Meta:
        verbose_name = 'Recurso'
        verbose_name_plural = 'Recursos'
    
    def __str__(self):
        return self.nome


class Planos(Base):
    plano = models.CharField('Plano', max_length=100)
    
    class Meta:
        verbose_name = 'Plano'
        verbose_name_plural = 'Planos'
        
    def __str__(self) -> str:
        return self.plano
    
    
class Precos(Base):
    ICONE_CHOICES = (
        ('lni-package', 'Caixa'),
        ('lni-drop', 'Gota'),
        ('lni-star', 'Estrela'),
    )
    
    preco = models.DecimalField('Recurso', max_digits=100, decimal_places=2)
    plano = models.ForeignKey('core.planos', verbose_name='Plano', on_delete=models.CASCADE)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Icone', max_length=16, choices=ICONE_CHOICES)
    
    class Meta:
        verbose_name = 'Preço'
        verbose_name_plural = 'Preços'
    
    def __str__(self):
        return str(self.preco)
    

class Cliente(Base):
    nome = models.CharField('Nome', max_length=100)
    profissao = models.CharField('Profissão', max_length=100)
    opiniao = models.TextField('Opinião', max_length=200)
    imagem = StdImageField('Imagem', upload_to='equipe', variations={'thumb': {'width': 40, 'height': 40, 'crop': True}})

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        
    def __str__(self) -> str:
        return self.nome
    