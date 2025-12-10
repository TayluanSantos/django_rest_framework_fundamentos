from rest_framework import serializers
from .models import Produto

class ProdutoSerializer(serializers.ModelSerializer):
    
    class Meta:
      model = Produto
      fields = ['id','nome','descricao','preco','estoque']

    def validate_estoque(self,value):
       
       if value <= 0 :
          raise serializers.ValidationError('O valor de estoque deve ser maior que 0')
       
       return value
    
    

    

