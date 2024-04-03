roupa = [
    {
        'acessorio': 'blusa',
        'tamanho': 'p',
        'marca': 'adidas',
        'preco': 50.55,
        'desconto': 0.10,
        'preco_com_desconto': ' '
    },
    {
        'acessorio': 'camisa',
        'tamanho': 'g',
        'marca': 'benetton',
        'preco': 60.10,
        'desconto': 0.05,
        'preco_com_desconto': ' ' 
    },
    {
        'acessorio': 'tenis',
        'tamanho': 'g',
        'marca': 'puma',
        'preco': 550.30,
        'desconto': 0.10,
        'preco_com_desconto': ' '
    },
    {
        'acessorio': 'calca',
        'tamanho': 'm',
        'marca': 'target',
        'preco': 336.67,
        'desconto': 0.08,
        'preco_com_desconto': ' '
    },
    {
        'acessorio': 'meia',
        'tamanho': 'm',
        'marca': 'bonds',
        'preco': 5.50,
        'desconto': 0.05,
        'preco_com_desconto': ' '
    }
    ]

#verificar o tamanho do acessório
for element in roupa:
    if element['tamanho'] == 'm':
        print('%s Tamanho médio.' % (element['acessorio']))
    elif element['tamanho'] == 'p':
        print('%s Tamanho pequeno.' % (element['acessorio']))
    elif element['tamanho'] == 'g':
        print('%s Tamanho grande.' % (element['acessorio']))

print()

#definir o valor final com desconto
for index, element in enumerate(roupa):
    preco = element['preco'] * element['desconto']
    roupa[index]['preco_com_desconto'] = element['preco'] - preco #explicar sobre o uso de roupa[index][peco_com_desconto]
    print(element)

print()
