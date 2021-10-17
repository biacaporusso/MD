# ----------------------- FUNÇÕES UTILIZADAS NAS DUAS IMPLEMENTAÇÕES ---------------------------

def primeiroRamo(sortedLista, capTotal):

    nos = []
    ramos = [] 

    for i in range(len(sortedLista)):
        if (sortedLista[i][0] <= capTotal):
            quant = int(capTotal/sortedLista[i][0])
        else:
            quant = 0

        nos.append(quant)
        capTotal = capTotal - quant*sortedLista[i][0]

    ramos.append(nos)

    return ramos

def interessesDosNos(ramos, quantItens, sortedLista):

    interesse = []
    for i in range(len(ramos)):
        valor = 0
        for j in range(quantItens):
        
            valor = valor + (ramos[i][j] * sortedLista[j][1])

        interesse.append(valor)

    return interesse

def maiorPeso(sortedLista):

    maiorPeso = -1
    for i in range(len(sortedLista)):
        if (sortedLista[i][0] > maiorPeso):
            maiorPeso = sortedLista[i][0]

    return maiorPeso

def capacidadeMochila(maiorPeso, sortedLista):

    somaPesos = 0
    for i in range(len(sortedLista)):
        somaPesos = somaPesos + sortedLista[i][0]

    if (somaPesos//2 < maiorPeso):
        capMochila = somaPesos
    else:
        capMochila = (somaPesos+maiorPeso)//2

    return capMochila


# ----------------------- FUNÇÕES PARA A IMPLEMENTAÇÃO DA BUSCA EXAUSTIVA ---------------------------

def analisarRamo (ramos, capTotal, quantItens, sortedLista):

    for i in range(quantItens-2, -1, -1):

        if ramos[-1][i] != 0:  # se tiver um diferente de 0

            #capFinal = capacidadeFinal(ramos, quant, capacidade, sortedLista)
            #print("capFinal =", capFinal)

            nos = []
            for j in range(i):  # adiciona os valores até chegar nesse diferente de 0
                nos.append(ramos[-1][j])

            nos.append(ramos[-1][i] -1) # quando chegar nesse diferente de 0, tira 1 dele
            #agora ver quantos da pra inserir a partir dessa nova capacidade

            for k in range(i+1, quantItens):

                capFinal = capacidadeNo(nos, capTotal, sortedLista)

                if sortedLista[k][0] <= capFinal:
                    quantidade = int(capFinal/sortedLista[k][0])
                else:
                    quantidade = 0
                
                nos.append(quantidade)

            ramos.append(nos[:])
            nos.clear()
            
            break
            
def analisarNo(ramos, quantItens):  # serve para analisar se é o último ramo da arvore ou nao

    # vai ser o ultimo ramo se o todos os nós forem 0, exceto o ultimo

    for i in range(quantItens-1):

        if ramos[-1][i] == 0:
            verify = 0      # é o ultimo nó do ultimo ramo
        else:
            verify = 1      # não é o ultimo nó do ultimo ramo 
            break

    return verify

def capacidadeNo(nos, capTotal, sortedLista):

    for i in range(len(nos)):

        capTotal = capTotal - (nos[i]*sortedLista[i][0])

    capFinal = capTotal
    return capFinal

def maiorValor(interesse):

    maiorValor = -1
    for i in range(len(interesse)):

        if (interesse[i] >= maiorValor):
            maiorValor = interesse[i]

    return maiorValor

def itemValioso(interesse, maiorValor):

    for i in range(len(interesse)):

        if (interesse[i] == maiorValor):

            posicItem = i

    return posicItem


# ----------------------- FUNÇÕES PARA A IMPLEMENTAÇÃO DO LIMITANTE SUPERIOR -----------------------------

def calculoMaisValioso(infos):

    valor = infos[1] / infos[0]

    return valor

def acharPosicDiferenteZero(ramos, quantItens):

    for i in range(quantItens-2, -1, -1):

        if ramos[-1][i] != 0:  # se tiver um diferente de 0
            k = i
            break
    
    return k

def calculoLimitanteSuperior(k, ramos, quantItens, capTotal, sortedLista):

    # 1ª PARTE: SOMATÓRIO DO Z DO INÍCIO DO RAMO ATÉ K-1
    somatorio1 = 0
    for i in range(k):
        somatorio1 = somatorio1 + (sortedLista[i][1] * ramos[-1][i])
    parte1 = somatorio1

    #2ª PARTE: VALOR NA POSIÇÃO K
    parte2 = sortedLista[k][1] * (ramos[-1][k] - 1)


    #3ª PARTE: FÓRMULA (A PARTIR DE K+1 PRA FRENTE)
    valorProx = sortedLista[k+1][2]                   # valor do item que vem depois do K
    somatorio2 = 0
    for i in range(k):
        somatorio2= somatorio2 + (sortedLista[i][0] * ramos[-1][i])
    
    ultimoValor = sortedLista[k][0] * ramos[-1][k-1]
    parte3 = valorProx * (capTotal - (somatorio2 + ultimoValor))


    #  LIMITANTE SUPERIOR (SOMA DAS 3 PARTES)
    limitSuperior = round((parte1 + parte2 + parte3), 3)

    return limitSuperior

def compararZeS(Z, S):

    # Z = valor do ramo e S = limitante superior

    if (S > Z[-1]):
        return 1  #solução correta
    else:
        return 0  #solução incorreta
