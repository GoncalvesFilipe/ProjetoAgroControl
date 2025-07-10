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
    nome = models.CharField(max_length=100, default='Sem nome')
    descricao = models.CharField(max_length=100)
    preco = models.DecimalField("Preço", max_digits=10, decimal_places=2, default=0.00)
    quant_estoque = models.IntegerField()
    setor_destinado = models.CharField(max_length=300)
    data_entrada = models.DateField(auto_now=True)
    data_saida = models.DateField(auto_now=True)
    data_modificacao = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.descricao

class Movimento(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT, related_name='movimentos')
    data_entrada = models.DateField(auto_now_add=True)
    data_saida = models.DateField()
    quantidade = models.IntegerField()
    
    def __str__(self):
        return f"{self.produto.descricao} - {self.quantidade}"
    
class Funcionario(models.Model):
    nome_funcionario = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    cargo = models.CharField(max_length=50)
    data_admissao = models.DateField()

    def __str__(self):
        return self.nome_funcionario

class Venda(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, null=True)
    quantidade = models.PositiveIntegerField()
    preco_total = models.DecimalField(max_digits=10, decimal_places=2)
    data_venda = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.produto.nome} - {self.quantidade} und"
    
    def total_venda(self):
        return sum(item.subtotal() for item in self.itens.all())

    
class ItemVenda(models.Model):
    venda = models.ForeignKey('Venda', related_name='itens', on_delete=models.CASCADE)
    produto = models.ForeignKey('Produto', on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def subtotal(self):
        return self.quantidade * self.preco_unitario

    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome} - R${self.subtotal():.2f}"
