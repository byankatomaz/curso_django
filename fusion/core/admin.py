from django.contrib import admin

from .models import Cargo, Servico, Funcionario, Recursos, Planos, Precos, Cliente

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo', 'modificado')


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'icone', 'ativo', 'modificado')


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'ativo', 'modificado')


@admin.register(Recursos)
class RecursosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'ativo', 'icone')

@admin.register(Planos)
class PlanosAdmin(admin.ModelAdmin):
    list_display = ('plano', 'ativo', 'modificado')

@admin.register(Precos)
class PrecoAdmin(admin.ModelAdmin):
    list_display = ('preco', 'plano', 'ativo', 'icone')

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'profissao', 'opiniao', 'ativo', 'modificado')
