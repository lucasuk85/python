frase = 'o homem quando esta em paz nao quer guerra com ninguem'
vogais = ['a','e','i','o','u']
contagem = 0
vogal = ''

for index, element in enumerate(vogais):
    contagem2 = 0
    for element2 in frase:
        if vogais[index] == element2:
            contagem2 += 1
        if contagem < contagem2:
            contagem = contagem2
            vogal = vogais[index]
print(vogal, contagem)