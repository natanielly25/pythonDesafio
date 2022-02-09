print('=-= '* 10)
print('Analisando se comprimentos de 3 retas formam triangulo')
print('=-= '* 10)
a = float(input('Primeiro comprimento:'))
b = float(input('Segundo comprimento:'))
c = float(input('Terceiro comprimento:'))
if  a + b > c and b + c > a and a + c > b:
    print('As retas \33[32mFORMAM\33[m um triangulo')
else:
    print('As retas \33[31mNÃO\33[m formão um triangulo.')