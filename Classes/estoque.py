from segmentTree import SegTree

class Estoque:
    def __init__(self):
        self._produtos, self._segment_tree, self._produto_indices = [], None, {}

    def adicionar_produto(self, produto):
        if produto.codigo in self._produto_indices: 
            print('Produto já cadastrado!')
        else:
            self._produtos.append(produto)
            
            indice_produto = len(self._produtos) - 1
            self._produto_indices[produto.codigo] = indice_produto
            
            if self._segment_tree is None:
                self._segment_tree = SegTree([produto.quantidade])
            else:
                self._segment_tree = SegTree([p.quantidade for p in self._produtos])
                
    def remover_produto(self, codigo):
        for produto in self._produtos:
            if produto.codigo == codigo:
                
                self._produtos.remove(produto)
                
                indice_produto = self._produto_indices[codigo]
                self._segment_tree.set(indice_produto, 0)

                del self._produto_indices[codigo]
                print('Produto {} removido do estoque'.format(produto.nome))
                return
        print('Produto com código {} não encontrado no estoque.'.format(codigo))

    def empty(self): return len(self._produtos) == 0

    def listar_produtos(self):
        if self.empty():
            print('O estoque está vazio.')
        else:
            for produto in self._produtos: 
                print(produto)

    def buscar_produto(self, codigo):
        for produto in self._produtos:
            if produto.codigo == codigo:
                return produto
        return None

    def atualizar_quantidade(self, codigo, nova_quantidade):
        produto = self.buscar_produto(codigo)
        if produto:
            produto.quantidade = nova_quantidade
            indice_produto = self._produto_indices[codigo]
            self._segment_tree.set(indice_produto, nova_quantidade)
            print('Quantidade do produto {} atualizada para {}.'.format(produto.nome, nova_quantidade))
        else:
            print('Produto com código {} não encontrado no estoque.'.format(codigo))

    def valor_total_estoque(self):
        return sum(produto.preco * produto.quantidade for produto in self._produtos)

    def consultar_quantidade_produto(self, codigo):
        produto = self.buscar_produto(codigo)
        if produto:
            return produto.quantidade
        else:
            print('Produto com código {} não encontrado.'.format(codigo))
            return 0

    def consultar_quantidade_intervalo(self, codigo_inicio, codigo_fim):
        
        indice_inicio = self._produto_indices.get(codigo_inicio)
        indice_fim = self._produto_indices.get(codigo_fim)

        if indice_inicio is not None and indice_fim is not None:
            return self._segment_tree.range_sum(indice_inicio, indice_fim)
        else:
            print('Produto(s) com código(s) {} ou {} não encontrado(s).'.format(codigo_inicio, codigo_fim))
            return 0
    
    def quantidade_presente_estoque(self):
        return self._segment_tree.root()

    def consultar_produto_com_quantidade_minima(self, quantidade_minima):
        produtos_acima_do_minimo = []
        
        for produto in self._produtos:
            if produto.quantidade <= quantidade_minima:
                produtos_acima_do_minimo.append(produto)

        if produtos_acima_do_minimo:
            print('Produtos com quantidade menor ou igual a {}:'.format(quantidade_minima))
            for produto in produtos_acima_do_minimo:
                print('{} (Código: {}) - Quantidade: {}'.format(produto.nome, produto.codigo, produto.quantidade))
        else:
            print('Nenhum produto com quantidade menor ou igual a {} foi encontrado.'.format(quantidade_minima))
