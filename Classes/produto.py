class Produto:
    def __init__(self, codigo, nome, preco, quantidade):
        self._codigo, self._nome, self._preco, self._quantidade = codigo, nome, preco, quantidade

    @property
    def codigo(self):
        return self._codigo

    @property
    def nome(self):
        return self._nome

    @property
    def preco(self):
        return self._preco

    @property
    def quantidade(self):
        return self._quantidade
    
    @quantidade.setter
    def quantidade(self, valor):
        if valor < 0:
            raise ValueError("Quantidade não pode ser negativa.")
        self._quantidade = valor
    
    def __str__(self):
        return 'Produto: {} (Código: {}) | Preço: R${:.2f} | Quantidade: {}'.format(self._nome, self._codigo, self._preco, self._quantidade)

    
