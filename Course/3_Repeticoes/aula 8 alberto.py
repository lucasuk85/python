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

#descobrir quais planetsa sao rochosos e quais sao gasosos
rochosos = []
gasosos = []

for element in planeta:
    if element['superficie'] == 'rochosa':
        rochosos.append(element['nome'])
    else:
        gasosos.append(element['nome'])

print('Os planetas rochosos são:', ', '.join(rochosos)) #Em Python, ', '.join(lista) é uma maneira de concatenar os elementos de uma lista em uma única string, separando-os por uma vírgula seguida de um espaço. Isso é útil quando você tem uma lista de strings e deseja unir todas elas em uma única string com um certo separador entre cada elemento.
print('Os planetas gasosos são:', ', '.join(gasosos))

#obs: sempre que eu quiser imprimir uma lista numa só frase, devo criar um print fora do loop
#obs: para criar uma lista de novos elementos preciso criar fora do loop uma variavel com lista vazia para
#que seja concatenado

print()

#descobrir qual planeta está mais distante do sol
maior_distancia = 0
planeta_mais_distante = ''

for element in planeta:
    if element['distancia_do_sol'] > maior_distancia:
        maior_distancia = element['distancia_do_sol']
        planeta_mais_distante = element['nome']

print('O planeta %s é o mais distante do sol com'
      ' aproximadamente %i km de distância.' % (planeta_mais_distante, maior_distancia))

print()

#descobrir qual planeta possui mais satelites e imprimir qual é o nome e a quantidade
mais_satelites = 0

for element in planeta:
    if element['satelites'] > mais_satelites:
        mais_satelites =  element['satelites']
        qual_planeta = element['nome']

print('O planeta "%s" é o que possui a maior quandidade'
      ' de satélites, num total de: "%i".' % (qual_planeta, mais_satelites))

#descobrir qual planeta possui a maior e menor gravidade
maior_gravidade = planeta[0]['gravidade']
menor_gravidade = planeta[0]['gravidade']
nome_maior_gravidade = ''
nome_menor_gravidade = ''

for element in planeta:
    if element['gravidade'] > maior_gravidade:
        maior_gravidade = element['gravidade']
        nome_maior_gravidade = element['nome']
    if element['gravidade'] < menor_gravidade:
        menor_gravidade = element['gravidade']
        nome_menor_gravidade = element['nome']

print('O planeta com maior gravidade é %s com %.2f m/s².' % (nome_maior_gravidade, maior_gravidade))
print('O planeta com menor gravidade é %s com %.2f m/s².' % (nome_menor_gravidade, menor_gravidade))