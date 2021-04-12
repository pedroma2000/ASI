#Administração de Sistemas Informáticos, Exemplos Básicos
#Pedro "pedroma2000" Machado

import re

str = "8180238;Pedro Machado"

pattern = re.compile(r'^(?P<numero>.*);(?P<nome>.*)$')

lista_grupos = pattern.match(str)

if lista_grupos:
    print(lista_grupos.group(2), lista_grupos.group('numero'))