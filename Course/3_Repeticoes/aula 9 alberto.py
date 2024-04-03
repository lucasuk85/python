carros = [
    {
        'nome': 'audace',
        'motor': '1.0',
        'turbo': True,
        'flex': True,
        'preco': 135990
    },
    {
        'nome': 'pulse',
        'motor': 1.3,
        'turbo': False,
        'flex': True,
        'preco': 131990
    },
    {
        'nome': 'cronos',
        'motor': '1.0',
        'turbo': False,
        'flex': True,
        'preco': 96990
    },
    {
        'nome': 'pulse abarth',
        'motor': '1.3',
        'turbo': True,
        'flex': True,
        'preco': 149990
    },
    {
        'nome': 'strada',
        'motor': '1.3',
        'turbo': True,
        'flex': True,
        'preco': 135000
    },
    {
        'nome': 'titano',
        'motor': '2.2',
        'turbo': True,
        'flex': True,
        'preco': 259990
    },
    {
        'nome': '500',
        'motor': '1.4',
        'turbo': False,
        'flex': True,
        'preco': 82000
    },
    {
        'nome': 'uno',
        'motor': '1.0',
        'turbo': False,
        'flex': False,
        'preco': 20000
    }
]
#colocar uma chave ID para todos os dicionarios da lista

for index, element in enumerate(carros):
    element['id'] = index + 1
    
print(carros) 


print('Carros flex:')
print()

for index, element in enumerate(carros):
    if element['flex'] == True:
        print(element['id'], element['nome'], 'flex')


print()

print('Carros flex e turbo:')
print()

count = 0
for index, element in enumerate(carros):
    if element['turbo'] == True and element['flex'] == True:
        count += 1
        carros[index]['id'] = count
        print(element['id'], element['nome'], 'turbo e flex')

