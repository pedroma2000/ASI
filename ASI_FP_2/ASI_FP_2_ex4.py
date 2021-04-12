#Administração de Sistemas Informáticos, 2ª Semana, Exercício 4
#Pedro "pedroma2000" Machado

#Estrutura de dados que representa a tabela do enunciado
translations = {"filme": ["film", "movie"], "locomotiva": ["locomotive", "train"],
                "pessoa": ["person", "individual"]}

#Imprimir a estrutura criada no ecrã
for word, translation in translations.items():
    print("Português: %s" % word)

    for t in translation:
        print("Tradução: %s" % t)

    print()

#Imprimir as traduções de "locomotiva"
print("Português: locomotiva")
print("Traduções: %s" % (", ".join(translations["locomotiva"])))