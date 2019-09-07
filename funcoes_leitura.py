from estado import Estado
from automato import Automato

#Método auxiliar para tirar as linhas em branco (\n) da leitura do arquivo txt
def arrumaLinhas(linhas):
    while ('' in linhas):
        linhas.remove('')
    return linhas

#Cria os objetos dos estados e salva em uma lista
def getEstados(linhas):
    estados = {}
    i = 3
    while(i < len(linhas)):
        linha = linhas[i].split(',')
        if (linha[0] not in estados):
            estados[linha[0]] = Estado(linha[0])
        if (linha[2] not in estados):
            estados[linha[2]] = Estado(linha[2])

        i = i + 1 
    return estados

#Verifica se todas as transições de cada estado foram cadastradas e garante que seja um AFD
def verificaAutomato(estados, alfabeto):
    erro = False
    for v in estados.values():
        if (len(v.vizinhos) != len(alfabeto)):
            print("Erro: É necessário cadastrar todas as transições para o estado " + str(v))
            erro = True

    return erro

def getEstadosFinais(linhaFinais, estados):
    listaFinais = {}
    for i in linhaFinais:
        listaFinais[i] = estados[i]

    return listaFinais

#Pega as linhas do arquivo de texto e organiza para elas poderem ser lidas
def getInput(arquivo):
    linhas = arquivo.read().splitlines()
    linhas = arrumaLinhas(linhas)
    alfabeto = linhas[0].split(',')
    inicial = linhas[1].strip("inicial=")
    linhaFinais = linhas[2].strip("final=").split(',')
    estados = getEstados(linhas)
    inicial = estados[inicial]
    del linhas[0:3]
    finais = getEstadosFinais(linhaFinais, estados)

    return linhas, estados, alfabeto, inicial, finais;

#Aplica as transições do arquivo de texto para todos os estados do autômato
def aplicaTransicoes(linhas, estados):
    for linha in linhas:
        linha = linha.split(',')
        estados[linha[0]].vizinhos[linha[1]] = estados[linha[2]]

#Lê e testa as palavras digitadas no console
def lerPalavras(automato):
    print("Digite '/sair' para parar a leitura")
    palavra = ''

    while (palavra != "/sair"):
        palavra = input("Digite a palavra a ser testada no automato: ")
        
        if (palavra != "/sair"): automato.testar(palavra)
        else: break

#Inicia a leitura do arquivo de texto
def init(arquivo):
    with open(arquivo) as arquivo:
        linhas, estados, alfabeto, inicial, finais = getInput(arquivo)

        automato = Automato(alfabeto, inicial, finais)

        aplicaTransicoes(linhas, estados)
        
        #Se o automato tiver todos os estados cadastrados, então o usuário poderá ler as palavras para teste
        if (verificaAutomato(estados, alfabeto) == False):
            lerPalavras(automato)