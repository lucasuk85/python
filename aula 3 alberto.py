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

for index, element in enumerate(lista2):
    if index < 3:
        print(index, element)

for index, element in enumerate(lista2):
    if index == 3:
        print(element)

lista6 = ['cachoror', 'papagaio', 'macaco', 'urubu']
