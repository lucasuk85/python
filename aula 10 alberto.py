planeta = [
    {
        'nome': 'mercurio',
        'distancia_do_sol': 57909227,
        'tamanho': 48794,
        'gravidade': 3.7,
        'satelites': 0,
        'superficie': 'rochosa'
    },
    {
        'nome': 'venus',
        'distancia_do_sol': 108200000,
        'tamanho': 12104,
        'gravidade': 8.87,
        'satelites': 0,
        'superficie': 'rochosa'
    },
    {
        'nome': 'terra',
        'distancia_do_sol': 149600000,
        'tamanho': 12742,
        'gravidade': 9.807,
        'satelites': 1,
        'superficie': 'rochosa'
    },
    {
        'nome': 'marte',
        'distancia_do_sol': 227940000,
        'tamanho': 6779,
        'gravidade': 3.71,
        'satelites': 2,
        'superficie': 'rochosa'
    },
    {
        'nome': 'jupiter',
        'distancia_do_sol': 778330000,
        'tamanho': 139820,
        'gravidade': 24.79,
        'satelites': 95,
        'superficie': 'rochosa'
    },
    {
        'nome': 'netuno',
        'distancia_do_sol': 4504300000,
        'tamanho': 49244,
        'gravidade': 11.15,
        'satelites': 14,
        'superficie': 'gasoso'
    },
    {
        'nome': 'saturno',
        'distancia_do_sol': 1429400000,
        'tamanho': 116460,
        'gravidade': 10.44,
        'satelites': 145,
        'superficie': 'gasoso'
    },
    {
        'nome': 'urano',
        'distancia_do_sol': 2870990000,
        'tamanho': 50724,
        'gravidade': 8.87,
        'satelites': 28,
        'superficie': 'gasoso'
    }
    ]

for index in range(0, len(planeta)):
    element = planeta[index]
    element['id'] = index + 1
    print(element)

#criar tabuada 1 a 10

numero = 5

for element in range(1, 11):
    resultado = numero * element
    print('%i x %i = %s' % (numero, element, resultado))

