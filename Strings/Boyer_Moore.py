NUMERO_DE_CARACTERES = 256

def heuristica_caractere_ruim(string, tamanho):
    caractere_ruim = [-1]*NUMERO_DE_CARACTERES

    for i in range(tamanho):
        caractere_ruim[ord(string[i])] = i

    return caractere_ruim

def preprocessar_sufixo_forte(deslocamento, pos_b, padrao, m):
    i = m
    j = m + 1
    pos_b[i] = j

    while i > 0:
        while j <= m and padrao[i - 1] != padrao[j - 1]:
            if deslocamento[j] == 0:
                deslocamento[j] = j - i

            j = pos_b[j]
             
        i -= 1
        j -= 1
        pos_b[i] = j

def preprocessar_caso2(deslocamento, pos_b, padrao, m):
    j = pos_b[0]
    for i in range(m + 1):
         
        if deslocamento[i] == 0:
            deslocamento[i] = j

        if i == j:
            j = pos_b[j]

def buscar(texto, padrao):
    deslocamento_inicial = 0
    m = len(padrao)
    n = len(texto)

    pos_b = [0] * (m + 1)

    deslocamento = [0] * (m + 1)

    preprocessar_sufixo_forte(deslocamento, pos_b, padrao, m)
    preprocessar_caso2(deslocamento, pos_b, padrao, m)

    caractere_ruim = heuristica_caractere_ruim(padrao, m)

    while deslocamento_inicial <= n - m:
        j = m - 1

        while j >= 0 and padrao[j] == texto[deslocamento_inicial + j]:
            j -= 1
        if j < 0:
            print("Padrão ocorre no deslocamento = %d" % deslocamento_inicial)
            deslocamento_inicial += deslocamento[0]
        else:
            deslocamento_inicial += max(deslocamento[j + 1], j - caractere_ruim[ord(texto[deslocamento_inicial+j])])
