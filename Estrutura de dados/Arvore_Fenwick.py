class ArvoreFenwick:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.arvore = [0] * (tamanho + 1)

    def build(self, dados):
        for i in range(1, self.tamanho + 1):
            self.update(i, dados[i - 1])

    def update(self, idx, delta):
        while idx <= self.tamanho:
            self.arvore[idx] += delta
            idx += idx & -idx

    def query(self, idx):
        soma = 0
        while idx > 0:
            soma += self.arvore[idx]
            idx -= idx & -idx
        return soma