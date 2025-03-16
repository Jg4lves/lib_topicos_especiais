def coeficiente_binomial_recursivo(n, k):
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    return coeficiente_binomial_recursivo(n - 1, k - 1) + coeficiente_binomial_recursivo(n - 1, k)