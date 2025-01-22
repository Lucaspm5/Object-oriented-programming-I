from graph import Graph
from estoque import Estoque

import networkx as nx
import matplotlib.pyplot as plt

class SistemaLogistico:
    def __init__(self):
        self.grafo, self.usuarios, self.estoque = Graph(), {}, Estoque()

    def cadastrar_usuario(self, usuario):
        assert usuario.cpf not in self.usuarios
        self.usuarios[usuario.cpf] = usuario

    def cadastrar_local(self, nome): 
        self.grafo.create_node(nome)

    def adicionar_conexao(self, local1, local2, distancia):
        self.grafo.add_edge(local1, local2, distancia)

    def remover_local(self, nome):
        self.grafo.remove_node(nome)
        
    def remover_conexao(self, local1, local2):
        self.grafo.remove_edge(local1, local2)
    
    def pertence(self, node):
        return node in self.grafo.get_nameNodes()
    
    def planejar_rota(self, origem, destino):
        if not self.pertence(origem) or not self.pertence(destino):
            raise ValueError("Local não encontrado no sistema.")

        self.grafo.clean()
        self.grafo.dijkstra(self.grafo.get_nameIndex(origem))
        
        rota = self.grafo.restore_path(self.grafo.get_nameIndex(origem), self.grafo.get_nameIndex(destino))
        
        return {'rota': rota, 'distancia': self.grafo.get_distance(destino)}

    def planejar_multiplas_entregas(self, caminhao, origem):
        if not self.pertence(origem):
            raise ValueError("Local de origem não encontrado no sistema.")
        
        partial = origem
        
        rotas = []
        
        for destino in caminhao.destinos:  
            if not self.pertence(destino):
                raise ValueError(f"Destino '{destino}' não encontrado no sistema.")
            
            self.grafo.clean()
            self.grafo.dijkstra(self.grafo.get_nameIndex(origem))
            
            rota = self.grafo.restore_path(self.grafo.get_nameIndex(origem), self.grafo.get_nameIndex(destino))
            distancia = self.grafo.get_distance(destino)
            
            rotas.append({'rota': rota, 'distancia': distancia})
            origem = destino
        
        self.grafo.clean()
        self.grafo.dijkstra(self.grafo.get_nameIndex(origem))
        
        rota = self.grafo.restore_path(self.grafo.get_nameIndex(origem), self.grafo.get_nameIndex(partial))
        distancia = self.grafo.get_distance(partial)
            
        rotas.append({'rota': rota, 'distancia': distancia})
        
        caminhao.rota_planejada = rotas  
        return rotas
    
    def map(self):
        G = nx.Graph()

        for local in self.grafo.get_nameNodes():
            G.add_node(local)

        for i, local in enumerate(self.grafo.get_nameNodes()):
            for node in self.grafo._neighbors[i]:
                if node.vertex in self.grafo._nameIndex.values():
                    vizinho = self.grafo.get_indexName(node.vertex)
                    distancia = node.distance
                    G.add_edge(local, vizinho, weight=distancia)

        pos = nx.spring_layout(G)
        labels = nx.get_edge_attributes(G, 'weight')

        plt.figure(figsize=(10, 8))
        nx.draw_networkx_nodes(G, pos, node_size=700, node_color='pink')
        nx.draw_networkx_edges(G, pos, width=2, alpha=0.5, edge_color='blue')
        nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        
        plt.title("- Mapa de Rotas -")
        plt.show()

    def listar_funcionarios(self):
        if self.usuarios:
            print("\nFuncionários Cadastrados:")
            for cpf, funcionario in self.usuarios.items():
                print("Nome: {}, CPF: {}, Cargo: {}".format(funcionario.nome, cpf, funcionario.cargo))
        else:
            print("Não há funcionários cadastrados.")
