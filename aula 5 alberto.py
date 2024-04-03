gato = [
    {
        'nome': 'bidu',
        'tamanho': 25,
        'idade': 3,
        'cor': ['branco', 'cinza'],
        'proprietario': 'Carlos'
    },
    {
        'nome': 'kay',
        'tamanho': 20,
        'idade': 2,
        'cor': ['branco', 'preto'],
        'proprietario': 'Maria'        
    },
    {
        'nome': 'tico',
        'tamanho': 23,
        'idade': 5,
        'cor': 'branco e marrom',
        'proprietario': 'Catia'
    },
    {
        'nome': 'kyra',
        'tamanho': 22,
        'idade': 6,
        'cor': 'branco',
        'proprietario': ''
    },
    {
        'nome': 'pepe',
        'tamanho': 26,
        'idade': 6,
        'cor': 'preto',
        'proprietario': ''
    }
    ]

#tamanho acima da media ou superior
for element in gato:
    if element['tamanho'] >= 25:
        print(element)

print()

#encontrar gatos que não possua dono e estão para adoção   
for index, element in enumerate(gato):
    if element['proprietario'] == '':
        gato[index]['proprietario'] = 'Adocao'
print(gato)

print()

#modificar o proprietario dos dois gatos para adoção, kyra para Angela e Pepe para Celio
for index, element in enumerate(gato):
    if element['nome'] == 'kyra':
        gato[index]['proprietario'] = 'Angela'
print(gato)

print()

for index, element in enumerate(gato):
    if element['nome'] == 'Pepe':
        gato[index]['proprietario'] = 'Celio'
print(gato)

print()

#passaram-se 3 anos, atualize a idade
for index, element in enumerate(gato):
    gato[index]['idade'] += 3
    print(element)