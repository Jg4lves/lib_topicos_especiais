def RABIN_KARP(T, P):
    n = len(T)
    b = len(P)
    
    if b == 0 or b > n:
        return []
    
    p = 10**9 + 7
    c = 256
    
    h = 1
    for _ in range(b - 1):
        h = (h * c) % p
    
    p_hash = 0
    t_hash = 0
    
    for i in range(b):
        p_hash = (c * p_hash + ord(P[i])) % p
        t_hash = (c * t_hash + ord(T[i])) % p
    
    ocorrencias = []
    
    for i in range(n - b + 1):
        if p_hash == t_hash:
            combina = True
            for j in range(b):
                if T[i + j] != P[j]:
                    combina = False
                    break
            if combina:
                ocorrencias.append(i)
        
        if i < n - b:
            t_hash = ((t_hash - ord(T[i]) * h) * c + ord(T[i + b])) % p
            if t_hash < 0:
                t_hash += p
    
    return ocorrencias
