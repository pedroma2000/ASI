#Administração de Sistemas Informáticos, Exemplos Básicos
#Pedro "pedroma2000" Machado

import re

str = "8180238;Pedro Machado"

pattern = re.compile(r'^(?P<numero>.*);(?P<nome>.*)$')
print(pattern.sub(r"\g<nome>;\g<numero>", str))