import rsa
import time
import json

def main():

    # LEITURA de K

    k = int(input('Quantidade k de numeros primos: '))


    # GERAR PRIMOS
    primos = rsa.gerarPrimos(k)
    print("Numeros primos gerados:", primos[0:k])


    # CALCULAR N
    N = rsa.calcularN(k, primos)
    print("N =", N)


    # CALCULAR PHI DE N
    phiN = rsa.calcularPhiN(k, primos)
    print("Phi de N =", phiN)


    # ACHAR COPRIMO DE PHI DE N
    coprimo = rsa.buscarCoprimoPhi(phiN)
    print("Coprimo de phi de N (e) =", coprimo)
    

    # ACHAR INVERSA DO COPRIMO DE PHI DE N
    inversa = rsa.calcularInversoE(phiN, coprimo)
    print("Inversa do coprimo (e^-1) =", inversa)


    # CALCULAR D
    D = rsa.calcularD(phiN, inversa)
    print("D =", D)


    # LEITURA E CRIPTOGRAFIA DA MENSAGEM
    mensagem = int(input('Mensagem: '))
    inicio = time.time()
    if mensagem < N:
        cript = rsa.criptografia(mensagem, N, coprimo)
        print("Mensagem criptografada:", cript)
    else:
        print("Erro (mensagem maior que o valor de N)")
        return


    # DECRIPTOGRAFIA DA MENSAGEM
    Dis = rsa.calcularDis(D, primos, k)

    As = rsa.calcularAs(cript, primos, k, Dis)

    Mis = rsa.calcularMis(primos, k)

    MisLinha = rsa.calcularMisLinha(Mis, primos, k)

    MLmenosUm = rsa.calcularMisLinhaMenosUm(MisLinha, primos, k)

    decript = rsa.decriptografia(As, Mis, MLmenosUm, primos, k)

    if (decript == mensagem):
        print("Mensagem decriptografada: ", decript)
    else:
        print("Erro")

    fim = time.time()
    diferenca = fim - inicio
    print("Tempo de execucao: {:.2f}" .format(diferenca))


main()



