credito = {'123': 750, '456': 812, '789': 980}

for chave, valor in credito.items():
  print(f'Para o documento {chave}, o valor do escore de crédito é {valor}.')
  print('\n')

for chave in credito.keys():
  print(chave)
  print(credito[chave])
  print(f'Para o documento {chave}, o valor do escore de crédito é {credito[chave]}.')
  print('\n')

for valor in credito.values():
  print(valor)
  print(f'O valor do escore de crédito é {valor}, mas não temos mais as chaves :(.')
  print('\n')