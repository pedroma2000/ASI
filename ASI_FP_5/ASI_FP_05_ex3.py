#Administração de Sistemas Informáticos, 5ª Semana, Exercício 3
#Pedro "pedroma2000" Machado

import re

# Contar o número de letras minúsculas de um texto a partir de expressões regulares (REGEX)

def countUpperCase(text):
    # Procura todas as maiúsculas
    upperCase = re.compile(r"[A-Z]")

    # O tamanho de todas as letras maíuculas encontradas no texto
    str = len(upperCase.findall(text))
    print(str)
