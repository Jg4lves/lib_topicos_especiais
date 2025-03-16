import heapq

def prim(grafo, raiz):
    num_vertices = len(grafo)
    chave = [float('inf')] * num_vertices
    pai = [-1] * num_vertices
    chave[raiz] = 0
    visitado = [False] * num_vertices
    fila_prioridade = [(0, raiz)]

    while fila_prioridade:
        chave_atual, u = heapq.heappop(fila_prioridade)
        if visitado[u]:
            continue
        visitado[u] = True

        for v, peso in grafo[u]:
            if not visitado[v] and peso < chave[v]:
                chave[v] = peso
                pai[v] = u
                heapq.heappush(fila_prioridade, (chave[v], v))

    return pai, chave