#Administração de Sistemas Informáticos, 6ª Semana, Exercício 3
#Pedro "pedroma2000" Machado

import re

pattern = re.compile(r'^(.*): \$(.*)$')
# ou pattern = re.compile(r'^(.*):\s\$(.*)$')

def convert(price):
    priceFloat = float(price) * 0.8182
    return round(priceFloat, 2)

with open("ex3.txt") as fp:
    for str in fp:
        list = pattern.match(str)
        price = convert(list.group(2))

        if list:
            print("Match: ", list.group(1), price, '€')

        else:
            print("Doesn't match")