#Administração de Sistemas Informáticos, 2ª Semana, Exercício 3
#Pedro "pedroma2000" Machado

import datetime

#Classificação de pessoas tendo em conta a sua idade
dates = ['12/08/2010', '21/06/1950', '05/06/2005', '03/01/1981', '21/05/2014']
year = datetime.date.today().year

for d in dates:
    #vai buscar o ano das datas (posição 2 separadas por /)
    yearDates = (int)(d.split('/')[2])
    age = year - yearDates
    #age = 2020 - yearDates

    if age >= 0 and age <= 12:
        print("Criança: ", age, "anos")
    elif age >= 13 and age <= 17:
        print("Juvenil: ", age, "anos")
    elif age >= 18 and age <= 64:
        print("Adulto: ", age, "anos")
    else:
        print("Sénior: ", age, "anos")


