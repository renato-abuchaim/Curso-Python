real = float(input('Quanto dinheiro você tem an carteira? R$'))
dolar = real / 5.47
euro = real / 6.36
print('Com R${:.2f} você pode comprar US${:.2f} ou €{:.2f}'.format(real, dolar, euro))