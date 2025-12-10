from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter() 
router.register('produtos', views.ProdutoViewSet, basename='produtos') # Com base nos métodos definidos no ProdutoViewset (implicitamente) será criada as rotas.

# Define a lista de rotas
urlpatterns = [
    path('', include(router.urls)) # Incluindo as rotas no urlpatterns
]


