import functions
import random
import time

def main():

    for cont in range(10):

        inicio = time.time()
        quantItens = int(input('\nQuantidade de itens: '))

        infos = list()
        lista = list()

        '''   # --------- caso quiser inserir as informações manualmente e nao de forma aleatoria -----
        for i in range(quantItens):
            infos.append(int(input('\nPeso do item: ')))
            infos.append(int(input('Interesse no item: ')))
            valor = round(functions.calculoMaisValioso(infos), 4)
            infos.append(valor)
            lista.append(infos[:])
            infos.clear()
        '''
        for i in range(quantItens):
            infos.append(random.randrange(10, 101))
            infos.append(random.randrange(10, 101))
            valor = round(functions.calculoMaisValioso(infos), 4)
            infos.append(valor)
            lista.append(infos[:])
            infos.clear()

        sortedLista = sorted(lista, key=lambda item: (-item[2], item[0]))
        print("\nLista classificada como: [peso, interesse, valor final do item]")
        print("Sorted lista (do mais valioso pro menos):", sortedLista)

        maiorPeso = functions.maiorPeso(sortedLista)
        capTotal = functions.capacidadeMochila(maiorPeso, sortedLista)
        print("\ncapacidade da mochila =", capTotal)

        galhos = functions.primeiroRamo(sortedLista, capTotal)

        print("\nprimeiro galho: ", galhos)

        k = functions.acharPosicDiferenteZero(galhos, quantItens)
        
        limitanteSuperior = functions.calculoLimitanteSuperior(k, galhos, quantItens, capTotal, sortedLista)
        print("\nlimitante superior (S) =", limitanteSuperior)

        interesse = []
        interesse = functions.interessesDosNos(galhos, quantItens, sortedLista)

        print("interesse (Z) =", interesse[-1])

        verify = functions.compararZeS(interesse, limitanteSuperior)

        # verify = 1 : solucao correta
        # verify = 0 : soluçao errada
        while (verify != 1):
            print("\nRamo:", galhos[-1]) 
            print("ainda nao e a solucao correta")
            functions.analisarRamo(galhos, capTotal, quantItens, sortedLista)
            k = functions.acharPosicDiferenteZero(galhos, quantItens)
            limitanteSuperior = functions.calculoLimitanteSuperior(k, galhos, quantItens, capTotal, sortedLista)
            interesse = functions.interessesDosNos(galhos, quantItens, sortedLista)
            print("interesse (Z) =", interesse[-1])
            verify = functions.analisarNo(galhos, quantItens)

        print("\nSolucao correta: ramo", galhos[-1])

        fim = time.time()
        diferenca = fim - inicio
        print("tempo de execucao:", diferenca)
        arquivo = open('LimitanteSuperior.txt', 'a')
        arquivo.write(str(diferenca))
        arquivo.write("\n")
        arquivo.close()

main()