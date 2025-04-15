def soma_lista(numeros: list) -> int:
  s = 0
  for numero in numeros:
    s = s + numero
  return s

soma = soma_lista(numeros=[2] * 20)
print(soma)