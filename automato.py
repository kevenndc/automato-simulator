from estado import Estado

class Automato:
    def __init__(self, alfabeto, inicial, final):
        self.alfabeto = alfabeto
        self.inicial = inicial
        self.final = final
        self.atual = self.inicial

    def testar(self, palavra):
        self.atual = self.inicial

        for letra in palavra:
            if(letra not in self.alfabeto):
                print("A palavra digitada possui letras que não fazem parte do alfabeto do automato")
                self.atual = self.inicial
                break
            else:
                self.atual = self.atual.getProximo(letra)

        if(self.atual.nome in self.final):
            print("Aprovado!")
        else:
            print("Rejeitado!")