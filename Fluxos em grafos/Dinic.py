class Aresta:
    def __init__(self, destino, fluxo, capacidade, reversa):
        self.destino = destino
        self.fluxo = fluxo
        self.capacidade = capacidade
        self.reversa = reversa

class Grafo:
    def __init__(self, vertices):
        self.adjacencias = [[] for _ in range(vertices)]
        self.vertices = vertices
        self.niveis = [0] * vertices

    def adicionar_aresta(self, origem, destino, capacidade):
        aresta_direta = Aresta(destino, 0, capacidade, len(self.adjacencias[destino]))
        
        aresta_reversa = Aresta(origem, 0, 0, len(self.adjacencias[origem]))
        
        self.adjacencias[origem].append(aresta_direta)
        self.adjacencias[destino].append(aresta_reversa)

    def busca_em_largura(self, origem, destino):
        for i in range(self.vertices):
            self.niveis[i] = -1

        self.niveis[origem] = 0
        fila = [origem]

        while fila:
            atual = fila.pop(0)
            for aresta in self.adjacencias[atual]:
                if self.niveis[aresta.destino] < 0 and aresta.fluxo < aresta.capacidade:
                    self.niveis[aresta.destino] = self.niveis[atual] + 1
                    fila.append(aresta.destino)

        return self.niveis[destino] >= 0

    def enviar_fluxo(self, origem, fluxo, destino, inicio):
        if origem == destino:
            return fluxo

        while inicio[origem] < len(self.adjacencias[origem]):
            aresta = self.adjacencias[origem][inicio[origem]]

            if self.niveis[aresta.destino] == self.niveis[origem] + 1 and aresta.fluxo < aresta.capacidade:
                fluxo_atual = min(fluxo, aresta.capacidade - aresta.fluxo)
                fluxo_temporario = self.enviar_fluxo(aresta.destino, fluxo_atual, destino, inicio)

                if fluxo_temporario > 0:
                    aresta.fluxo += fluxo_temporario
                    self.adjacencias[aresta.destino][aresta.reversa].fluxo -= fluxo_temporario
                    return fluxo_temporario

            inicio[origem] += 1

        return 0

    def fluxo_maximo_dinic(self, origem, destino):
        if origem == destino:
            return -1

        fluxo_total = 0

        while self.busca_em_largura(origem, destino):
            inicio = [0] * (self.vertices + 1)
            while True:
                fluxo = self.enviar_fluxo(origem, float('inf'), destino, inicio)
                if fluxo == 0:
                    break
                fluxo_total += fluxo

        return fluxo_total