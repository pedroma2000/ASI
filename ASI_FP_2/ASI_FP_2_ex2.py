#Administração de Sistemas Informáticos, 2ª Semana, Exercício 2
#Pedro "pedroma2000" Machado

array = [8, 7, 8, 6, 10, 12, 14, 12, 18, 12, 17]

#Calcular e imprimir a tabela de frequências por nota
for num in range(21):
    print(num, ",", array.count(num))