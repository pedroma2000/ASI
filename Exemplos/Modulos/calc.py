#Administração de Sistemas Informáticos, Exemplos Básicos
#Pedro "pedroma2000" Machado

def soma(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    try:
        r = a / b
    except ZeroDivisionError:
        r = "Divisão por zero"
    return r

