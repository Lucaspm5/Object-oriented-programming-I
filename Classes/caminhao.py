class Caminhao:
    def __init__(self, placa):
        self._placa = placa
        self._destinos, self.rota_planejada = [], []

    @property
    def placa(self):
        return self._placa
    @property
    def destinos(self):
        return self._destinos
    @property
    def rota_planejada(self):
        return self._rota_planejada
    
    @destinos.setter
    def destinos(self, destinos):
        self._destinos = destinos

    @rota_planejada.setter
    def rota_planejada(self, rotas):
        self._rota_planejada = rotas

    def adicionar_destino(self, destino):
        self._destinos.append(destino)

    def visualizar_rotas(self):
        if not self._rota_planejada:
            return "Nenhuma rota planejada."
        
        visualizacao = "Caminhão {}:\n".format(self.placa)
        for i, rota in enumerate(self._rota_planejada, 1):
            caminho = " -> ".join(rota['rota'])
            visualizacao += "Entrega {}: {} | Distância: {} km\n".format(i, caminho, rota['distancia'])
        
        return visualizacao

