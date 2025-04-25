numero_e_par = lambda numero: True if numero % 2 == 0 else False

numeros = range(0, 10)

for numero in numeros:
  if numero_e_par(numero) == True:
    print(f'O número {numero} é par!')