class Estado:
    def __init__(self, nome):
        self.vizinhos = {}
        self.nome = nome

    def getProximo(self, valor):
        return self.vizinhos[valor]

    def __str__(self):
        return self.nome
    
    def __repr__(self):
        return self.nome
