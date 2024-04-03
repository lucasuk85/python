frutas = [
    {
        'nome': 'abacaxi',
        'origem': 'paraguai',
        'citrico': 'sim',
        'preco': 4.58,
        'plantio': 'marco'
    },
    {
        'nome': 'abacate',
        'origem': 'mexico',
        'citrico': 'nao',
        'preco': 2.77,
        'plantio': 'fevereiro'        
    },
    {
        'nome': 'amora',
        'origem': 'persia',
        'citrico': 'nao',
        'preco': 0.03,
        'plantio': 'junho'
    },
    {
        'nome': 'banana',
        'origem': 'paraguai',
        'citrico': 'sim',
        'preco': 4.58,
        'plantio': 'marco'
    },
    {
        'nome': 'damasco',
        'origem': 'china',
        'citrico': 'sim',
        'preco': 33.53,
        'plantio': 'maio'
    }
    ]

outono = ['marco', 'abril', 'maio', 'junho']
inverno = ['julho', 'agosto', 'setembro']
primavera = ['outubro', 'novembro', 'dezembro']
inverno = ['janeiro', 'fevereiro']


#preço acima de 20 reais retorna fruta cara(o)
for element in frutas:
    if element['preco'] > 20.00:
        print('A fruta %s é cara(o)' % (element['nome']))

print()

#se a fruta é ou não cítrica
for element in frutas:
    if element['citrico'] == 'sim':
        print(element)
    
print()

#qual a estação do ano a fruta representa
for element in frutas:
    if element['plantio'] in outono:
        print('a fruta %s tem por indicação o plantio no outono' % (element['nome']))
    elif element['plantio'] in inverno:
        print('a fruta %s tem por indicação o plantio no inverno' % (element['nome']))
    elif element['plantio'] in primavera:
        print('a fruta %s tem por indicação o plantio no primavera' % (element['nome']))
    else:
        print('a fruta %s tem por indicação o plantio no inverno' % (element['nome']))

print()

#qual a origem da fruta
lista_origem = []

for index, element in enumerate(frutas):
    lista_origem.append(element['origem'])

print(lista_origem)