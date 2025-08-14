n = input('Digiti algo ')
print(f'É string: {n.isalpha()}')
print(f'É letras maiúsculas: {n.isupper()}')
print(f'É numeros: {n.isnumeric()}')
print(f'É numeros ou letras: {n.isalnum()}')

print('É numeros ou letras: {}'.format(n.isalnum()))