from estado import Estado

dist_states = {}
all_states = {}
non_dist_states = {}

#Faz a primeira distinção entre estados finais e não finais e armazena todas as combinações de estados em um dicionário
def primeiraDinstincao(x, y, automato):
    for estado_x in x:
        for estado_y in y:
            if (estado_x == estado_y): pass
            else:
                if ((estado_y, estado_x) not in all_states):
                    if (ehDistinguivel(estado_x, estado_y, automato)): 
                        dist_states[(estado_x, estado_y)] = True
                        all_states[(estado_x, estado_y)] = True
                    else:
                        non_dist_states[(estado_x, estado_y)] = False
                        all_states[(estado_x, estado_y)] = False


def ehDistinguivel(p, q, automato):
    if ((p in automato.final.values() and q not in automato.final.values()) or (q in automato.final.values() and p not in automato.final.values())):
        return True
    else:
        return False

#arrumar aqui!
def buscaEquivalentes(automato):
    remove_list = {}
    while(True):
        marcado = False
        for each in non_dist_states.keys():
            if (non_dist_states[(each[0], each[1])] == False):
                for simbolo in automato.alfabeto:

                    if (((each[0].vizinhos[simbolo], each[1].vizinhos[simbolo]) in dist_states) or ((each[1].vizinhos[simbolo], each[0].vizinhos[simbolo]) in dist_states)):
                        dist_states[(each[0], each[1])] = True
                        non_dist_states[(each[0], each[1])] = True
                        marcado = True
                        
        if (marcado == False):
            break

#Cria uma lista com todos os estados que não foram distinguíveis depois da função buscaEquivatentes()
def getEstadosNaoDistinguiveis():
    nova_lista = {}
    for key, value in non_dist_states.items():
        if (value == False):
            nova_lista[key] = False

    return nova_lista

def getXY(estados):
    x = []
    y = []    

    for index, (key, value) in enumerate(estados.items()):
        if (index > 0):
            x.append(value)

    for index, (key, value) in enumerate(estados.items()):
        if (index < (estados.__len__() - 1)):
            y.append(value)

    return x, y;

def start(estados, automato):
    
    x, y = getXY(estados)

    primeiraDinstincao(x, y, automato);

    buscaEquivalentes(automato)
    non_dist_states = getEstadosNaoDistinguiveis()

    print('--------------------ESTADOS EQUIVALENTES-----------------------')

    for estados in non_dist_states.keys():
        print(estados)

    print('---------------------ESTADOS DIFERENCIAVEIS----------------------')
    
    print (dist_states)
