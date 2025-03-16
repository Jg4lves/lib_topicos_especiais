class Grafo:
    def __init__(self, tamanho):
        self.matriz_adj = [[0] * tamanho for _ in range(tamanho)]
        self.tamanho = tamanho
        self.dados_vertices = [''] * tamanho

    def adicionar_aresta(self, u, v, capacidade):
        self.matriz_adj[u][v] = capacidade

    def adicionar_dado_vertice(self, vertice, dado):
        if 0 <= vertice < self.tamanho:
            self.dados_vertices[vertice] = dado

    def busca_em_largura(self, origem, destino, pai):
        visitado = [False] * self.tamanho
        fila = []  # Usando lista como fila
        fila.append(origem)
        visitado[origem] = True

        while fila:
            u = fila.pop(0)  # Remove do início da lista

            for indice, valor in enumerate(self.matriz_adj[u]):
                if not visitado[indice] and valor > 0:
                    fila.append(indice)
                    visitado[indice] = True
                    pai[indice] = u

        return visitado[destino]

    def edmonds_karp(self, origem, destino):
        pai = [-1] * self.tamanho
        fluxo_maximo = 0

        while self.busca_em_largura(origem, destino, pai):
            fluxo_caminho = float("Inf")
            s = destino
            while(s != origem):
                fluxo_caminho = min(fluxo_caminho, self.matriz_adj[pai[s]][s])
                s = pai[s]

            fluxo_maximo += fluxo_caminho
            v = destino
            while(v != origem):
                u = pai[v]
                self.matriz_adj[u][v] -= fluxo_caminho
                self.matriz_adj[v][u] += fluxo_caminho
                v = pai[v]

            caminho = []
            v = destino
            while(v != origem):
                caminho.append(v)
                v = pai[v]
            caminho.append(origem)
            caminho.reverse()
            nomes_caminho = [self.dados_vertices[nodo] for nodo in caminho]
            print("Caminho:", " -> ".join(nomes_caminho), ", Fluxo:", fluxo_caminho)

        return fluxo_maximo