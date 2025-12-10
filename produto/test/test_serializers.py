import pytest
from unittest.mock import patch
from produto.serializers import ProdutoSerializer
from produto.models import Produto


def test_product_serializer_is_valid():

    """Testa a validade do campos"""

    # Arrange
    data = {
        'nome': 'Notebook Gamer',
        'descricao': 'Notebook para o gamer ideal',
        'preco': 5000.00,
        'estoque': 10,
    }

    serializer = ProdutoSerializer(data = data)

    # Assert
    assert serializer.is_valid() 
    assert serializer.validated_data['nome'] == 'Notebook Gamer'
    assert serializer.validated_data['descricao'] == 'Notebook para o gamer ideal'
    assert serializer.validated_data['preco'] == 5000.00
    assert serializer.validated_data['estoque'] == 10


def test_produto_serializer_create(produto_mock):
    """Testa a criação de um novo produto"""

    # Arrange
    data = {
        'nome': 'Notebook Gamer',
        'descricao': 'Notebook para o gamer ideal',
        'preco': 5000.00,
        'estoque': 10,
    }

    # Act
    with patch.object(ProdutoSerializer, 'save', return_value=produto_mock):
        serializer = ProdutoSerializer(data=data)
        assert serializer.is_valid()
        
        produto = serializer.save()

    # Assert
    assert produto.id is not None
    assert produto.nome == 'Notebook Gamer'
    assert produto.descricao == 'Notebook para o gamer ideal'
    assert produto.preco == 5000.00
    assert produto.estoque == 10


def test_serializer_required_fields():

    """Testa que campos obrigatórios são validados"""
    
    # Arrange
    serializer = ProdutoSerializer(data={})

    # Assert
    assert not serializer.is_valid()
    
    assert "nome" in serializer.errors
    assert "preco" in serializer.errors
    assert "estoque" in serializer.errors


def test_serializer_stock_field_validation():

    """Testa a validação do campo estoque"""
    
    # Arrange
    data = {
        'nome': 'Notebook Gamer',
        'descricao': 'Notebook para o gamer ideal',
        'preco': 5000.00,
        'estoque': 0,
    }

    serializer = ProdutoSerializer(data = data)

    # Assert
    assert not serializer.is_valid() 
    assert serializer.errors['estoque'][0] == 'O valor de estoque deve ser maior que 0'



    


