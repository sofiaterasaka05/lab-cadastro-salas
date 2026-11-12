import pytest

from salas import CadastroSalas


def test_cadastra_sala():
    cadastro = CadastroSalas()
    assert cadastro.cadastrar("A101", 30) == {
        "codigo": "A101",
        "capacidade": 30
    }


def test_rejeita_duplicado_e_preserva_original():
    cadastro = CadastroSalas()
    cadastro.cadastrar("A101", 30)

    with pytest.raises(ValueError, match="Sala já cadastrada"):
        cadastro.cadastrar("A101", 50)

    assert cadastro._salas["A101"] == {
        "codigo": "A101",
        "capacidade": 30
    }


def test_rejeita_capacidade_zero():
    cadastro = CadastroSalas()

    with pytest.raises(ValueError, match="Capacidade deve ser positiva"):
        cadastro.cadastrar("A101", 0)

    assert cadastro.cadastrar("A101", 30)["capacidade"] == 30


def test_rejeita_capacidade_negativa():
    cadastro = CadastroSalas()

    with pytest.raises(ValueError, match="Capacidade deve ser positiva"):
        cadastro.cadastrar("A101", -1)

    assert cadastro.cadastrar("A101", 30)["capacidade"] == 30