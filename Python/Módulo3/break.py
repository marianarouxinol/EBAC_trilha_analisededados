numeros = [361, 553, 194, 13, 510, 33, 135]

for numero in numeros:

  if numero % 2 == 0:
    print(f'O numero {numero} é par')
    break
  else:
    continue
    print(f'O numero {numero} é impar')