import math

def retornaPrimo(n) :

    for i in range(2, n):

        if (n%i == 0):
            # se nao for primo
            verify = 0
            break
        else :
            # se for primo
            verify = 1    
    return verify

def gerarPrimos(k):

    n=3
    i=0

    primos = [] 
    while (i < k):

        ehprimo = retornaPrimo(n)

        if (ehprimo == 1):
           primos.append(n)
           i = i+1

        n = n+1
    return primos

def calcularN(k, primos):

    N=1

    for i in range(k):
        N = N * primos[i]

    return N

def calcularPhiN(k, primos):

    phiN = 1

    for i in range(k):
        phiN = phiN * (primos[i] - 1)

    return phiN

def buscarCoprimoPhi(phiN):

    for b in range(3, phiN):

        ehprimo = retornaPrimo(b)
        if ehprimo == 1 :

            r = phiN % b
            antigoB = b

            while r != 0 :
                antigoR = r            # antigoR = 3
                r = antigoB % antigoR  # r = 8 % 3
                antigoB = antigoR
        
            if antigoB == 1 : 
                # significa que o MDC = 1 portanto são coprimos
                coprimo = b
                break  # sai do loop for 

    return coprimo

def calcularInversoE(phiN, e):

    # N é o N e "e" é o coprimo

    for i in range(phiN): 
        resto = (i * e) % phiN
        if (resto == 1) :
            inverso = i
            break

    return inverso

def calcularD(phiN, inverso):

    d = inverso % phiN

    return d

def criptografia(msg, N, e):

    C = pow(msg, e) % N

    return C

def calcularDis(d, primos, k):

    dis = []

    for i in range(k):
        dis.append(d % (primos[i] -1))

    return dis

def calcularAs(C, primos, k, Dis):

    As = []

    for i in range(k):
        As.append(pow(C, Dis[i]) % primos[i])

    return As

def calcularMis(primos, k):

    Mis = []

    produtoPrimos=1

    for i in range(k):
        produtoPrimos = produtoPrimos * primos[i]

    for i in range(k):
        Mis.append(produtoPrimos/primos[i])

    return Mis

def calcularMisLinha(Mis, primos, k):

    misLinha = []

    for i in range(k):
        misLinha.append(Mis[i]%primos[i])

    return misLinha

def calcularMisLinhaMenosUm(Mis, primos, k):

    MisLinhaMenosUm = []

    for i in range(k):

        x=1
        
        result = (x * Mis[i]) % primos[i] 

        if result != 1:

            while result != 1:
            
                x = x+1
                result = (x * Mis[i]) % primos[i]

        MisLinhaMenosUm.append(x)
    
    return MisLinhaMenosUm



def decriptografia(As, Mis, misMenosUm, primos, k):

    produto = []
    
    for i in range(k):
        produto.append(As[i] * Mis[i] * misMenosUm[i])
    
    soma=0
    for i in range(k):
        soma = soma+produto[i]

    produtoDosPrimos=1
    for i in range(k):
        produtoDosPrimos = produtoDosPrimos * primos[i]

    mensagemDecriptografada = soma % produtoDosPrimos

    return mensagemDecriptografada

