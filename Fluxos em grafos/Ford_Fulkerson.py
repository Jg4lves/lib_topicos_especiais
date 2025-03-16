from collections import defaultdict


class Grafo:

    def __init__(self, grafo):
        self.grafo = grafo
        self.LINHAS = len(grafo)

    def busca_em_largura(self, origem, destino, pai):

        visitado = [False] * (self.LINHAS)
        fila = []

        fila.append(origem)
        visitado[origem] = True

        while fila:
            u = fila.pop(0)

            for indice, valor in enumerate(self.grafo[u]):
                if not visitado[indice] and valor > 0:
                    fila.append(indice)
                    visitado[indice] = True
                    pai[indice] = u

        return True if visitado[destino] else False

    def ford_fulkerson(self, origem, destino):
        pai = [-1] * (self.LINHAS)
        fluxo_maximo = 0

        while self.busca_em_largura(origem, destino, pai):
            fluxo_caminho = float("Inf")
            s = destino
            while s != origem:
                fluxo_caminho = min(fluxo_caminho, self.grafo[pai[s]][s])
                s = pai[s]

            fluxo_maximo += fluxo_caminho

            v = destino
            while v != origem:
                u = pai[v]
                self.grafo[u][v] -= fluxo_caminho
                self.grafo[v][u] += fluxo_caminho
                v = pai[v]

        return fluxo_maximo