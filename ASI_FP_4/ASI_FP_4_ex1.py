#Administração de Sistemas Informáticos, 4ª Semana, Exercício 1
#Pedro "pedroma2000" Machado

import sys

# cálculo do preço final
def calc1():
    print("Introduza o valor correspondente ao preço base: ")
    precoBase = sys.stdin.readline().strip()
    precoFinal = "(" + precoBase + " * 23%) - 10"

    print(precoFinal)

    precoFinal = precoFinal.replace("%", " * 0.01 + " + precoBase)

    print(precoFinal)
    print("Preço final: ", (eval(precoFinal)))


#versão 2
def calc2():
    print("Introduza o valor correspondente ao preço base: ")
    precoBase = sys.stdin.readline().strip()
    precoFinal = "(" + precoBase + " * 23%) - 10"

    print(precoFinal)

    precoFinal = precoFinal.replace("%", " / 100 + " + precoBase)

    print(precoFinal)
    print("Preço final: ", (eval(precoFinal)))

calc1()
calc2()