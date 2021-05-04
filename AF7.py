'''
1) Criar um Algoritmo que imprima a soma entre dois valores quaisquer digitados pelo usuário. Utilizar uma função 
para fazer a soma. 

2) Criar um Algoritmo que apresenta a divisão entre dois valores quaisquer digitados pelo usuário. Utilizar uma 
função para fazer a divisão.

3) Criar um Algoritmo que, a partir dos valores de peso (em kg) e de altura (em m) de uma pessoa digitados pelo 
usuário, imprima o IMC daquela pessoa e também sua classificação conforme a diretriz de saúde abaixo. Utilizar duas 
funções: uma para calcular e retornar o IMC, e outra para obter e retornar à classificação de peso do indivíduo.

4) Criar um Algoritmo que, a partir dos coeficientes ʻaʼ, ʻbʼ e ʻcʼ de uma equação do 2º. grau digitados pelo 
usuário, apresenta na tela quantas raízes reais existem e quais são seus valores. Utilizar uma única função para 
resolver o problema. Obs.: utilize a função str( ) para converter um número em texto.

5) Criar um Algoritmo que calcula e apresenta na tela a média entre N valores inteiros de idade (em anos) lidos do 
usuário. Utilize uma única função para calcular e retornar a média. 

6) Criar um Algoritmo que, a partir de dois números quaisquer e também de uma operação aritmética(+, -, *, /), 
digitados pelo usuário, apresenta na tela o resultado do cálculo solicitado. Utilize quatro funções, uma para cada 
função matemática. Exemplos de execução.
'''
import numpy as np

escolha = int(input("Escolha a atividade (1-6): "))
if(escolha>6 or escolha<1):
    exit("Atividade não existente")
'''
---------------------------------------------ALGORITMO Exercício 1:
#VARIAVEIS
numero_um = 0
numero_dois = 0

#PROGRAMA
    definir soma(um, dois)
        retorna um + dois

numero_um <- leia("numero acima de zero")
numero_dois <- leia("numero acima de zero")

se numero_um = 0 e numero_dois = 0 faca
    exit("um dos valores era zero")
senao
    imprima(soma(numero_um, numero_dois))
fim

'''
if(escolha==1):
    def soma(um, dois):
        return um + dois

    numeroum = int(input("Digite um número acima de zero: "))
    numerodois = int(input("Digite outro número acima de zero: "))
    if(numeroum == 0 or numerodois == 0):
        exit("Um dos valores era zero")
    else:
        print("A soma de",numeroum,"com",numerodois,"é:",soma(numeroum, numerodois))
'''
---------------------------------------------ALGORITMO Exercício 2:
#VARIAVEIS
numero_um = 0
numero_dois = 0

#PROGRAMA
    definir divisao(um, dois)
        retorna um / dois

numero_um <- leia("numero acima de zero")
numero_dois <- leia("numero acima de zero")

se numero_um = 0 e numero_dois = 0 faca
    exit("um dos valores era zero")
senao
    imprima(divisao(numero_um, numero_dois))
fim
'''
if(escolha==2):
    def divisao(um, dois):
        return um / dois

    numeroum = int(input("Digite um número acima de zero: "))
    numerodois = int(input("Digite outro número acima de zero: "))
    if(numeroum == 0 or numerodois == 0):
        exit("Um dos valores era zero")
    else:
        print("A divisão de",numeroum,"com",numerodois,"é:",divisao(numeroum, numerodois))
'''
---------------------------------------------ALGORITMO Exercício 3:
#VARIAVEL
peso = 0
altura = 0

#PROGRAMA
    definir IMC(altura, peso):
        imc <- peso / (altura**2)
        retorna imc

    definir classificação(imc):
        se imc<18.5 faca
            retorna "Magreza"
        senao se imc>=18.5 e imc<25 faca
            retorna "Normal"
        senao se imc>=25 e imc<30 faca
            retorna "Sobrepeso"
        senao se imc>=30 e imc<40 faca
            retorna "Obesidade"
        senao faca
            retorna "Obesidade Grave"
        fim

    peso = leia ("Digite seu peso")
    altura = leia ("Digite sua altura: "))

    se peso == 0 ou altura == 0:
        exit("ERRO NO CALCULO: Altura ou Peso == 0 não são possiveis")
    senao:
        imc = IMC(altura, peso)
        imprima (classificação(imc))
'''
if(escolha==3):
    def IMC(altura, peso):
        imc = round(peso/(altura**2),2)
        return imc

    def classificação(imc):
        if(imc<18.5):
            return "Magreza"
        elif(imc>=18.5 and imc<25):
            return "Normal"
        elif(imc>=25 and imc<30):
            return "Sobrepeso"
        elif(imc>=30 and imc<40):
            return "Obesidade"
        else:
            return "Obesidade Grave"

    peso = float(input("Digite seu peso (em kg): "))
    altura = float(input("Digite sua altura (em m): "))

    if(peso == 0 or altura == 0):
        exit("ERRO NO CALCULO: Altura ou Peso == 0 não são possiveis")
    else:
        imc = IMC(altura, peso)
        print("Com o IMC de",imc,", sua classificação é:",classificação(imc))
'''
---------------------------------------------ALGORITMO Exercício 4:
#VARIAVEIS
a = 0
b = 0
c = 0

#PROGRAMA
se escolha==4 faca
    definir bhaskara(A, B, C):
        delta <- B**2 - 4 * A * C
        se delta<=0 faca
            exit("Não possui raizes")
        senao

        delta = sqrt(delta)
        x1 =  (-B + delta)/2*A
        x2 = (-B - delta)/2*A

        retorna x1, x2

    a = leia("Digite o valor A: ")
    b = leia("Digite o valor B: ")
    c = leia("Digite o valor C: ")

    imprima(bhaskara(a,b,c))
'''
if(escolha==4):
    def bhaskara(A, B, C):
        delta = B**2 - 4 * A * C
        if(delta<=0):
            exit("Não possui raizes")

        delta = np.sqrt(delta)
        x1 = (-B + delta)/2*A
        x2 = (-B - delta)/2*A

        return x1, x2

    a = int(input("Digite o valor A: "))
    b = int(input("Digite o valor B: "))
    c = int(input("Digite o valor C: "))

    print("As raizes de",a,",",b,"e",c,"são: ",bhaskara(a,b,c))
'''
---------------------------------------------ALGORITMO Exercício 5:
#VARIAVEIS
valores = 0
x = 0
repeticao = 0

#PROGRAMA
   definir media(repete):
        enquanto (repeticao > x) faca
            valores = valores + leia("Digite sua idade: ")
            x += 1
        retorno soma/repete

    repeticao = leia("Digite quantas vezes devemos receber o sua idade: ")
    imprima("A média é: ", media(repeticao))
'''
if(escolha==5):

    def media(repete):
        valores = []
        x = 0
        while repeticao > x:
            valores.append(int(input("Digite sua idade: ")))
            x += 1
        soma = sum(valores)
        return soma/repete

    repeticao = int(input("Digite quantas vezes devemos receber o sua idade: "))
    print("A média é: ",media(repeticao))
'''
---------------------------------------------ALGORITMO Exercício 6:
#VARIAVEIS
numeroum = 0
numerodois = 0
operador = 0

#PROGRAMA
    definicao soma(a, b):
        retorno imprima("A soma é",a + b)

    definicao subtracao(a, b):
        retorno imprima("A subtração é",a - b)

    definicao multiplicacao(a, b):
        retorno imprima("A multiplicação é",a * b)
        
    definicao divisao(a, b):
        retorno imprima("A divisão é",a / b)

    numeroum = leia("Digite um número: ")
    operador = leia("Digite uma operação (+, -, *, /): ")
    numerodois = leia("Digite outro número: ")

    numeroum = inteiro(numeroum)
    numerodois = inteiro(numerodois)

    se operador == "+" faca
        soma(numeroum, numerodois)
    senao se operador == "-" faca
        subtracao(numeroum, numerodois)
    senao se operador == "*" faca
        multiplicacao(numeroum, numerodois)
    senao se operador == "/" faca
        divisao(numeroum, numerodois)
'''
if(escolha==6):
  
#    formula = input("Digite um número: ")
#    formula += input("Digite uma operação (+, -, *, /): ")
#    formula += input("Digite outro número: ")
#    print("O resultado de",formula,"é:", eval(formula))

    def soma(a, b):
        return print("A soma é",a + b)
    def subtracao(a, b):
        return print("A subtração é",a - b)
    def multiplicacao(a, b):
        return print("A multiplicação é",a * b)
    def divisao(a, b):
        return print("A divisão é",a / b)

    numeroum = input("Digite um número: ")
    operador = input("Digite uma operação (+, -, *, /): ")
    numerodois = input("Digite outro número: ")

    numeroum = int(numeroum)
    numerodois = int(numerodois)

    if(operador == "+"):
        soma(numeroum, numerodois)
    elif(operador == "-"):
        subtracao(numeroum, numerodois)
    elif(operador == "*"):
        multiplicacao(numeroum, numerodois)
    elif(operador == "/"):
        divisao(numeroum, numerodois)