from django.db import models

# Create your models here.

class Produto (models.Model):

    nome = models.CharField(max_length=200) 
    descricao = models.TextField(blank=True,null=True)
    preco = models.DecimalField(max_digits=9,decimal_places=2)
    estoque = models.IntegerField()

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
    
    def __str__(self):
        return self.nome