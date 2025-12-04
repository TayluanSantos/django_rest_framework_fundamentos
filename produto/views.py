from .models import Produto
from .serializers import ProdutoSerializer
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.shortcuts import get_object_or_404
# from rest_framework import generics
from rest_framework import viewsets


# ------------ 
#   APIVIEW
#  ------------
# class ProdutoList(APIView):

#     def get(self,request,format=None):
#         produtos = Produto.objects.all() 
#         serializer = ProdutoSerializer(produtos,many=True) # O argumento 'many'indica que é um lista (queryset) de objetos, e não com uma única instância individual de um modelo 
#         return Response(serializer.data) 
    
#     def post(self,request,format=None):
#         serializer = ProdutoSerializer(data=request.data) # Recebe os dados enviados na request
#         if serializer.is_valid(): 
#             serializer.save()
#             return Response(serializer.data, status= status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
# class ProdutoDetail(APIView):
    
#     def get(self, request, pk,format=None):
#         produto = get_object_or_404(Produto, pk=pk) # Busca objeto, se não encontrar, devolve um 404
#         serializer = ProdutoSerializer(produto)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         produto = get_object_or_404(Produto, pk=pk)
#         serializer = ProdutoSerializer(produto, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self,request,pk,format=None):
#         produto = get_object_or_404(Produto, pk=pk)
#         produto.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# ------------ 
#   GENERICS
#  ------------

# class ProdutoList(generics.ListCreateAPIView):
#     queryset = Produto.objects.order_by("-preco")
#     serializer_class = ProdutoSerializer

# class ProdutoDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Produto.objects.all()
#     serializer_class = ProdutoSerializer

# ------------ 
#   VIEWSET
#  ------------

class ProdutoViewSet(viewsets.ModelViewSet): 

    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer




