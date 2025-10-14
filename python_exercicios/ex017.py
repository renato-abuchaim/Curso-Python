import math
co = float(input('Comprimento do cateto oposrto: '))
ca = float(input('Comprimento do cateto adjacnete: '))
hi = math.hypot(co, ca)
print(f'{hi:.2f}')

# ou


'''
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co**2 + ca**2)**(1/2)
print(f'{hi:.2f}')
'''