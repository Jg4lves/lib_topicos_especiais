class SegmentTree:
    def __init__(self, arr):
        self.tamanho = len(arr)
        self.arvore = [(0, float('inf'), -float('inf'))] * (4 * self.tamanho)
        self.lazy = [0] * (4 * self.tamanho) 
        self.build(arr, 1, 0, self.tamanho - 1)

    def build(self, arr, no, inicio, fim):
        if inicio == fim:
            self.arvore[no] = (arr[inicio], arr[inicio], arr[inicio])
        else:
            meio = (inicio + fim) // 2
            self.build(arr, 2 * no, inicio, meio)
            self.build(arr, 2 * no + 1, meio + 1, fim)
            soma_esq, min_esq, max_esq = self.arvore[2 * no]
            soma_dir, min_dir, max_dir = self.arvore[2 * no + 1]
            self.arvore[no] = (
                soma_esq + soma_dir,  
                min(min_esq, min_dir), 
                max(max_esq, max_dir)  
            )

    def propagar(self, no, inicio, fim, meio):
        if self.lazy[no] != 0:
            valor = self.lazy[no]
            self.arvore[2 * no] = (
                self.arvore[2 * no][0] + valor * (meio - inicio + 1),
                self.arvore[2 * no][1] + valor, 
                self.arvore[2 * no][2] + valor 
            )
            self.arvore[2 * no + 1] = (
                self.arvore[2 * no + 1][0] + valor * (fim - meio),  
                self.arvore[2 * no + 1][1] + valor,  
                self.arvore[2 * no + 1][2] + valor  
            )
            self.lazy[2 * no] += valor
            self.lazy[2 * no + 1] += valor
            self.lazy[no] = 0  

    def atualizar_intervalo(self, no, inicio, fim, l, r, valor):
        if r < inicio or fim < l:
            return
        if l <= inicio and fim <= r:
            self.arvore[no] = (
                self.arvore[no][0] + valor * (fim - inicio + 1),  # Soma
                self.arvore[no][1] + valor,  
                self.arvore[no][2] + valor 
            )
            self.lazy[no] += valor  
            return
        meio = (inicio + fim) // 2
        self.propagar(no, inicio, fim, meio)
        self.atualizar_intervalo(2 * no, inicio, meio, l, r, valor)
        self.atualizar_intervalo(2 * no + 1, meio + 1, fim, l, r, valor)
        soma_esq, min_esq, max_esq = self.arvore[2 * no]
        soma_dir, min_dir, max_dir = self.arvore[2 * no + 1]
        self.arvore[no] = (
            soma_esq + soma_dir,  
            min(min_esq, min_dir),
            max(max_esq, max_dir)  
        )

    def consultar_intervalo(self, no, inicio, fim, l, r, operacao):
        if r < inicio or fim < l:
            if operacao == "soma":
                return 0
            elif operacao == "min":
                return float('inf')
            elif operacao == "max":
                return -float('inf')
        if l <= inicio and fim <= r:
            if operacao == "soma":
                return self.arvore[no][0]
            elif operacao == "min":
                return self.arvore[no][1]
            elif operacao == "max":
                return self.arvore[no][2]
        meio = (inicio + fim) // 2
        self.propagar(no, inicio, fim, meio)
        esquerda = self.consultar_intervalo(2 * no, inicio, meio, l, r, operacao)
        direita = self.consultar_intervalo(2 * no + 1, meio + 1, fim, l, r, operacao)
        if operacao == "soma":
            return esquerda + direita
        elif operacao == "min":
            return min(esquerda, direita)
        elif operacao == "max":
            return max(esquerda, direita)

    def update(self, l, r, valor):
        self.atualizar_intervalo(1, 0, self.tamanho - 1, l, r, valor)

    def query(self, l, r, operacao):
        return self.consultar_intervalo(1, 0, self.tamanho - 1, l, r, operacao)