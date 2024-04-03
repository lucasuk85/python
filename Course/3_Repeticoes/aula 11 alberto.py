frase = 'No fim de semana, chega sexta-feira, e o baile come a vontade a noite inteira'
vogais = ['a','e','i','o','u']

contagem_a = 0
contagem_e = 0
contagem_i = 0
contagem_o = 0
contagem_u = 0
contagem = 0

for element in frase:
    if element in vogais:
        if element == 'a':
            contagem_a += 1
        if element == 'e':
            contagem_e += 1
        if element == 'i':
            contagem_i += 1
        if element == 'o':
            contagem_o += 1
        if element == 'u':
            contagem_u


if contagem_a > contagem_e and contagem_a > contagem_i and contagem_a > contagem_o and contagem_a > contagem_u:
    print('"A" apareceu %s vezes' % (contagem_a))
if contagem_e > contagem_a and contagem_e > contagem_i and contagem_e > contagem_o and contagem_e > contagem_u:
    print('"E" apareceu %s vezes' % (contagem_e))
if contagem_i > contagem_a and contagem_i > contagem_e and contagem_i > contagem_o and contagem_i > contagem_u:
    print('"I" apareceu %s vezes' % (contagem_i))
if contagem_o > contagem_a and contagem_o > contagem_e and contagem_o > contagem_i and contagem_o > contagem_u:
    print('"O" apareceu %s vezes' % (contagem_o))
if contagem_u > contagem_a and contagem_u > contagem_e and contagem_u > contagem_i and contagem_u > contagem_o:
    print('"U" apareceu %s vezes' % (contagem_u))