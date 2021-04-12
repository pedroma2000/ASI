#Administração de Sistemas Informáticos, 5ª Semana, Exercício 1
#Pedro "pedroma2000" Machado

import re

# Expressão regular que valide se o número de Cartão do Cidadão obedece ao padrão (N=número; A=Alfanumérico)

def validarCC(cc):
    # 8 números, espaço, 1 número, espaço, 2 letras, 2 números
    ccRegex = re.search("[0-9]{8}\s[0-9]\s[A-Z]{2}[0-9]", cc)

    #ccRegex = re.compile(r'^\d{8} \d [A-Z]{2}\d$')

    if (ccRegex):
        print("O número de cartão de cidadão obdece ao padrão.")
    else:
        print("O número de cartão de cidadão não obdece ao padrão.")
