from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__(self, nome, email, cpf):
        self._nome, self._email, self._cpf = nome, email, cpf

    @property
    def nome(self): return self._nome
    @property
    def email(self): return self._email
    @property
    def cpf(self): return self._cpf
        
    @abstractmethod
    def visualizar_rotas(self):
        pass

    def __repr__(self):
        return '{} nome = {} email = {} cpf = {}'.format(self.__class__.__name__, self.nome, self.email, self.cpf)
    # já vai comparar automaticamente 2 objetos da mesma classe pelo cpf
    def __eq__(self, other):
        if isinstance(other, Usuario):
            return self.cpf == other.cpf
        return False
    # Para instanciar uma classe como chave
    # x = Funcionario(...)
    # dict {x : 2} 
    def __hash__(self):
        return hash(self.cpf)
