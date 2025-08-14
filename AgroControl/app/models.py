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
    
    def __str__(self):
        return self.razao_social
    
class Produto(models.Model):
    descricao = models.CharField(max_length=100)
    quant_estoque = models.IntegerField()
    setor_destinado = models.CharField(max_length=300)
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)
    data_modificacao = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.descricao

class Movimento(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT, related_name='movimentos')
    data_entrada = models.DateField(auto_now_add=True)
    data_saida = models.DateField()
    quantidade = models.IntegerField()
    
    def __str__(self):
        return f"{self.produto.descricao} - {self.quantidade}"
    
class Setor(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
class Venda(models.Model):
    data_venda = models.DateField(auto_now_add=True)
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT, related_name='vendas')
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_vendida = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.produto.descricao} - {self.data_venda}"


class Entrada(models.Model):
    data_entrada = models.DateField(auto_now_add=True)
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT, related_name='entradas')
    quantidade = models.PositiveIntegerField()
    setor_origem = models.ForeignKey(Setor, on_delete=models.PROTECT, related_name='entradas')

    def __str__(self):
        return f"{self.produto.descricao} - Entrada: {self.quantidade}"