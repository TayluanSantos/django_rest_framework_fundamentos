from rest_framework import serializers
from .models import Produto

# Criando os serializers de forma mais abstraída, utilizando os ModelSerializer
class ProdutoSerializer(serializers.ModelSerializer):
    
    class Meta:
      model = Produto
      fields = '__all__' # O valor '__all__' indica que todos os campos serão serializados e desserilizados 


# Testando a abordagem de criar os serializers de forma manual
# class ProductSerializer(serializers.Serializer):

#   name = serializers.CharField(max_length=200,required=True,allow_blank=False,)
#   description = serializers.CharField(required=False,allow_blank=True,allow_null=True)
#   price = serializers.DecimalField(max_digits=9,decimal_places=2,required=True)
#   inventory = serializers.IntegerField(required=True)




