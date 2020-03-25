# da para fazer 5^2 assim: 5**2 ou pow(5,2)
# para fazer a raiz quadrada fazemos 25**(1/2)
# para fazer a raiz cubica fazemos 127**(1/3)
# para concatenar fazemos print('Oi'+'Olá') e o resultado é 'OiOlá'
# para multiplicar o texte que está num print fazemos print('Oi'*5) e o resultado é:
# OiOiOiOiOi
# Logo para fazer um titulo engraçado podemos fazer print('='*10+' Titulo '+'='*10) e o resultado é:
# ========== Titulo ==========

nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {:20}!'.format(nome))

print('Prazer em te conhecer {:<20}!'.format(nome))
print('Prazer em te conhecer {:>20}!'.format(nome))