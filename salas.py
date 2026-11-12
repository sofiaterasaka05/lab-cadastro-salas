
"""Cadastro simulado: cada instância guarda suas salas em memória."""


class CadastroSalas:
    def __init__(self):
        self._salas = {}

    def cadastrar(self, codigo: str, capacidade: int) -> dict:
        if capacidade <= 0:
            raise ValueError("Capacidade deve ser positiva")
        if codigo in self._salas:
            raise ValueError("Sala já cadastrada")
        sala = {"codigo": codigo, "capacidade": capacidade}
        self._salas[codigo] = sala
        return sala.copy()


if __name__ == "__main__":
    cadastro = CadastroSalas()
    print(cadastro.cadastrar("A101", 30))
