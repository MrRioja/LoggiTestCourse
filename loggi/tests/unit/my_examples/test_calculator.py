from unittest.mock import patch
import pytest

from my_examples.calculator import DivisionByZero, divisao, raiz_quadrada

@patch('my_examples.calculator.divisao', return_value=5)
def test_divisao(mock_divisao):
    result = mock_divisao(10, 2)

    assert result == 5
    assert mock_divisao.called_once()
    assert mock_divisao.called_once_with(10,2)

def test_divisao_raise_error():
     with pytest.raises(DivisionByZero):
        divisao(10, 0)


def test_raiz_quadrada():
    assert raiz_quadrada(81) == 9