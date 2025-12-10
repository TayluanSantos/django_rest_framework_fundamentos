import pytest
from unittest.mock import Mock

@pytest.fixture
def produto_mock():
    """Fixture que retorna um mock de produto."""
    
    produto_mock = Mock()
    produto_mock.id = 1
    produto_mock.nome = 'Notebook Gamer'
    produto_mock.descricao = 'Notebook para o gamer ideal'
    produto_mock.preco = 5000.00
    produto_mock.estoque = 10
    
    return produto_mock 