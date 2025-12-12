from django.db import models

# Create your models here.

class Categoria (models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=500)
    criado_em = models.DateField(auto_now_add=True)
    atualizado_em = models.DateField(auto_now=True)


    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nome

class Produto (models.Model):

    nome = models.CharField(max_length=255) 
    descricao = models.TextField(max_length=1000,blank=True,null=True)
    preco = models.DecimalField(max_digits=9,decimal_places=2)
    quantidade_estoque = models.IntegerField()
    criado_em = models.DateField(auto_now_add=True)
    atualizado_em = models.DateField(auto_now=True)
    categoria = models.ManyToManyField(Categoria)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
    
    def __str__(self):
        return self.nome

    
