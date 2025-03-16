def LPS(S, m):
    lps = [0] * m
    j = 0
    i = 1
    while i < m:
        if S[i] == S[j]:
            j += 1
            lps[i] = j
            i += 1
        else:
            if j != 0:
                j = lps[j-1]
            else:
                lps[i] = 0
                i += 1
    return lps

def KMP(T, n, S, m):
    lps = LPS(S, m)
    i = 0
    j = 0
    posicoes = []
    while i < n:
        if S[j] == T[i]:
            i += 1
            j += 1
            if j == m:
                posicoes.append(i - j)
                j = lps[j-1]
        else:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return posicoes