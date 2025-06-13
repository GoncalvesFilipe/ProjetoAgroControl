from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Usuario(AbstractUser):    
    nome = models.CharField(max_length=150)

    def __str__(self):
        return self.username
    
class Propriedade(models.Model):
    razao_social = models.CharField(max_length=50)
    endereco = models.CharField(max_length=300)
    telefone = models.CharField(max_length=15)
    email = models.CharField(max_length=25)
    
    def _str_(self):
        return self.razao_social
    
class Animal(models.Model):
    propriedade = models.ForeignKey(Propriedade, on_delete=models.PROTECT, related_name='animais')
    especie = models.CharField(max_length=30)
    raca = models.CharField(max_length=30)
    produto_aplicado = models.CharField(max_length=300)
    data_nascimento = models.DateField(auto_now=True)
    data_cadastro = models.DateField(auto_now=True)
    data_modificacao = models.DateField(auto_now=True)
    observacoes = models.TextField()
    
    def _str_(self):
        return f"{self.especie} - {self.raca}"
    
class Produto(models.Model):
    descricao = models.CharField(max_length=100)
    quant_estoque = models.IntegerField()
    setor_destinado = models.CharField(max_length=300)
    data_entrada = models.DateField(auto_now=True)
    data_saida = models.DateField(auto_now=True)
    data_modificacao = models.DateField(auto_now=True)
    
    def _str_(self):
        return self.descricao

class Movimento(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT, related_name='movimentos')
    data_entrada = models.DateField(auto_now_add=True)
    data_saida = models.DateField()
    quantidade = models.IntegerField()
    
    def _str_(self):
        return f"{self.produto.descricao} - {self.quantidade}"