from usuario import Usuario
from produto import Produto

class Funcionario(Usuario):
    def __init__(self, nome, email, cpf, cargo):
        super().__init__(nome, email, cpf)
        self._cargo = cargo

    @property
    def cargo(self): return self._cargo
    
    def cadastrar_local(self, sistema_logistico, nome):
        sistema_logistico.cadastrar_local(nome)
        return 'Local "{}" cadastrado com sucesso'.format(nome)

    def adicionar_conexao(self, sistema_logistico, local1, local2, distancia):
        sistema_logistico.adicionar_conexao(local1, local2, distancia)
        return 'Conexão entre "{}" e "{}" com distância {} unidades cadastrada.'.format(local1, local2, distancia)

    def remover_local(self, sistema_logistico, nome):
        sistema_logistico.remover_local(nome)
        return 'Local "{}" removido com sucesso.'.format(nome)

    def remover_conexao(self, sistema_logistico, local1, local2):
        sistema_logistico.remover_conexao(local1, local2)
        return 'Conexão entre "{}" e "{}" removida com sucesso.'.format(local1, local2)
    
    def visualizar_rotas(self, sistema_logistico, origem, destinos):
        return [sistema_logistico.planejar_rota(origem, destino) for destino in destinos]

    def adicionar_produto_no_estoque(self, estoque, produto):
        estoque.adicionar_produto(produto)

    def remover_produto_do_estoque(self, estoque, codigo):
        estoque.remover_produto(codigo)

    def listar_produtos_no_estoque(self, estoque):
        estoque.listar_produtos()

    def cadastrar_produto(self, estoque, codigo, nome, quantidade, preco_unitario):
        estoque.adicionar_produto(Produto(codigo, nome, preco_unitario, quantidade))

    def atualizar_quantidade_produto(self, estoque, codigo, quantidade):
        estoque.atualizar_quantidade(codigo, quantidade)

    def consultar_quantidade_produto(self, estoque, codigo):
        print(estoque.consultar_quantidade_produto(codigo))

    def consultar_quantidade_intervalo(self, estoque, codigo_inicio, codigo_fim):
        print(estoque.consultar_quantidade_intervalo(codigo_inicio, codigo_fim))  

    def calcular_valor_total_estoque(self, estoque):
        print(estoque.valor_total_estoque())  

    def remover_produto(self, estoque, codigo):
        estoque.remover_produto(codigo)  
    
    def exibir_quantidade(self, estoque):
        print(estoque.quantidade_presente_estoque())
    
    def consultar_produto_com_quantidade_minima(self, estoque, quantidade_minima):
        estoque.consultar_produto_com_quantidade_minima(quantidade_minima)
