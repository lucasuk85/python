caes = [
    {
        'nome': 'rex',
        'raca': 'poodle',
        'idade': 11,
        'vacina': True
    },
    {
        'nome': 'teco',
        'raca': 'golden',
        'idade': 3,
        'vacina': False
    },
    {
        'nome': 'tico',
        'raca': 'maltes',
        'idade': 5,
        'vacina': True
    },
    {
        'nome': 'zeus',
        'raca': 'chiauaua',
        'idade': 2,
        'vacina': True
    },
    {
        'nome': 'fly',
        'raca': 'pastor alemao',
        'idade': 4,
        'vacina': False
    }
]
#buscando caes sem vacina
for element in caes:
    if element['vacina'] == False:
        print(element)

print()

#buscando caes com idade superior a 5
for element in caes:
    if element['idade'] > 5:
        print(element)

print()

#printar os caes que sejam pastor ou poodle
for element in caes:
    if element['raca'] == 'poodle' or element['raca'] == 'pastor alemao':
        print(element)

print()

#imaginando que o mes passou, voce precisa deixar que todos os caes estao faltando a vacina
#alterar vacina pra False

for index, element in enumerate(caes):
    if element['vacina'] == True:
        caes[index]['vacina'] = False
print(caes)