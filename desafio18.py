import math
grau = float(input('Digite o o grau do angulo:'))
seno = math.sin(math.radians(grau))
print('O ângulo de {} tem o Seno de {:.2f}'.format(grau, seno))
cosseno = math.cos(math.radians(grau))
print('O ângulo de {} tem o Cosseno de {:.2f}'.format(grau, cosseno))
tangente = math.tan(math.radians(grau))
print('O ângulo de {} tem a Tangente de {:.2f}'.format(grau, tangente))
