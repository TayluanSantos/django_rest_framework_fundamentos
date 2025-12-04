from django.urls import path,include
# from .views import ProdutoList,ProdutoDetail
from rest_framework.routers import DefaultRouter
from . import views

# Ao trabalhar com ViewSets, posso utilizar o router para criar as rotas de forma automática
router = DefaultRouter() # Instanciando o DefaultRouter
router.register('produtos', views.ProdutoViewSet, basename='produtos') # Com base nos métodos definidos no ProdutoViewset (implicitamente) será criada as rotas.


# Define a lista de rotas
urlpatterns = [
    path('', include(router.urls)) # Incluindo as rotas no urlpatterns
]

# Utilizando a abordagem de criar manualmente as rotas para a GenericView e APIView
# urlpatterns = [
#     path('produtos/',ProdutoList.as_view(),name='produtos'),
#     path('produtos/<int:pk>/',ProdutoDetail.as_view(),name='produto')

# ]


