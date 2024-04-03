lista1 = [50, 40, 30, 20, 50, 40, 60]
lista2 = ['Brasil', 'Chile', 'Argentina', 'Uruguai', 'Venezuela']
lista3 = [
    {
        "pais": "Brasil",
        "populacao": 260000000
    },
    {
        "pais": "Chile",
        "populacao": 40000000
    },
    {
        "pais": "Argentina",
        "populacao": 42000000
    },
    {
        "pais": "EUA",
        "populacao": 420000000
    }
]
lista4 = [["Brasil", "Argentina"], ["França", "Itália"]]

lista5 = [True, False, True, True, False, True, False, False]

quantidade = 0

for pagantes in lista5:
    if not pagantes:
        quantidade += 1
        
print(quantidade)