'''
import math

ângulo = float(input('Digite o ângulo que você deseja: '))

seno = math.sin(math.radians(ângulo))
print(f'O ângulo de {ângulo} tem o SENO de {seno:.2f}')

cosseno = math.cos(math.radians(ângulo))
print(f'O ângulo de {ângulo} tem o COSSENO de {cosseno:.2f}')

tangente = math.tan(math.radians(ângulo))
print(f'O ângulo de {ângulo} tem a TANGENTE de {tangente:.2f}')
'''
# ou 

from math import radians, sin, cos, tan

ângulo = float(input('Digite o ângulo que você deseja: '))

seno = sin(radians(ângulo))
print(f'O ângulo de {ângulo} tem o SENO de {seno:.2f}')

cosseno = cos(radians(ângulo))
print(f'O ângulo de {ângulo} tem o COSSENO de {cosseno:.2f}')

tangente = tan(radians(ângulo))
print(f'O ângulo de {ângulo} tem a TANGENTE de {tangente:.2f}')
