'''
import math

num = float(input("Digite um valor: "))
print(f'O valor digitado foi {num} e a sua porção é {math.trunc(num)}')
'''
# ou 

'''
num = float(input("Digite um valor: "))
print(f'O valor digitado foi {num} e a sua porção é {int(num)}')
'''
# ou

num = float(input("Digite um valor: "))
print(f'O valor digitado foi {num} e a sua porção é {num:.0f}')