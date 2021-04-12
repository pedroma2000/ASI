#Administração de Sistemas Informáticos, 6ª Semana, Exercício 1
#Pedro "pedroma2000" Machado

import re

pattern = re.compile(r'^(?P<pri>.*);(?P<tel>\d{9}$)')

with open("dados.txt") as fp:
    for str in fp:
        if pattern.match(str):
            # retirar /n
            str = str.strip()
            # print("Match")
            # Substitui: primeiro grupo, adiciona 00351, segundo grupo
            print(pattern.sub(r"\g<pri>;00351\g<tel>", str))

        else:
            print("Doesn't match")
