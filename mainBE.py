import functions
import random
import time
import operator

def main():

    for cont in range(10):

        inicio = time.time()
        quantItens = int(input('\nQuantidade de itens: '))

        infos = list()
        lista = list()

        # ----------------- caso queira inserir os elementos, sem que sejam aleatórios
        '''
        for i in range(quantItens):
            infos.append(int(input('\nPeso do item: ')))
            infos.append(int(input('Interesse no item: ')))
            lista.append(infos[:])
            infos.clear()
        '''
        
        for i in range(quantItens):
            infos.append(random.randrange(10, 101))
            infos.append(random.randrange(10, 101))
            lista.append(infos[:])
            infos.clear()
        
        print("\nLista organizada em [peso, interesse]")
        sortedLista = sorted(lista, key=operator.itemgetter(1,0), reverse=True)
        print("lista: ", sortedLista)

        maiorPeso = functions.maiorPeso(sortedLista)
        capTotal = functions.capacidadeMochila(maiorPeso, sortedLista)
        print("\ncapacidade da mochila =", capTotal)


        #__________criação do primeiro ramo que servirá de base para o resto__________

        ramos = [] 
        ramos = functions.primeiroRamo(sortedLista, capTotal)


        #__________criação dos próximos ramos (árvore completa)__________

        verify = 1
        while (verify != 0):
            functions.analisarRamo(ramos, capTotal, quantItens, sortedLista)
            verify = functions.analisarNo(ramos, quantItens)
        

        print("\nArvore final (ramos): ")
        for i in range(len(ramos)):
            print(ramos[i])


        #__________cálculo do valor de cada ramo e resultado final__________

        interesse = []
        interesse = functions.interessesDosNos(ramos, quantItens, sortedLista)
        print("\nValor de cada galho:")
        print(interesse)
        maiorValor = functions.maiorValor(interesse)
        print("maior valor =", maiorValor)

        posicaoValioso = functions.itemValioso(interesse, maiorValor)
        print("\nPortanto, mais valioso = ", ramos[posicaoValioso])
        #print("(considerando a sortedLista)")

        fim = time.time()
        diferenca = fim - inicio
        print("Tempo de execucao: {:.2f}" .format(diferenca))

        arquivo = open('BuscaExaustiva.txt', 'a')
        arquivo.write(str(diferenca))
        arquivo.write("\n")
        arquivo.close()

main()