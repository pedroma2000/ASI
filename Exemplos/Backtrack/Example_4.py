#Administração de Sistemas Informáticos, Exemplos Básicos
#Pedro "pedroma2000" Machado

import re

str = "8180238;Pedro Machado;M;21;912345678"

pattern = re.compile(r'^(.*);(\d{9}$)')

if pattern.match(str):
    print("Match")
    print(pattern.sub(r"\1;00351\2", str))

else:
    print("Doesn't match")