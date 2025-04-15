#Você trabalha na bolsa de valores e precisa simular o retorno de um investimento para diversos cenários:

valor_inicial, taxa_juros_anual, anos = 1000.00, 0.05, 10

valor_final = valor_inicial
for ano in range(1, anos+1):
  valor_final = valor_final * (1 + taxa_juros_anual)
valor_final = round(valor_final, 2)
print(f'Para um valor inicial de R$ {valor_inicial} e uma taxa de juros anual de {taxa_juros_anual}, em {anos} anos você terá R$ {valor_final}') 

valor_inicial, taxa_juros_anual, anos = 1020.00, 0.03, 10

valor_final = valor_inicial
for ano in range(1, anos+1):
  valor_final = valor_final * (1 + taxa_juros_anual)
valor_final = round(valor_final, 2)
print(f'Para um valor inicial de R$ {valor_inicial} e uma taxa de juros anual de {taxa_juros_anual}, em {anos} anos você terá R$ {valor_final}') 

#Como podemos fazer para reaproveitar o código e evitar repetições?


  
def juros_compostos_anual(valor_inicial: float, taxa_juros_anual: float, anos: int) -> float:
  valor_final = valor_inicial
  for ano in range(1, anos+1):
    valor_final = valor_final * (1 + taxa_juros_anual)
  valor_final = round(valor_final, 2)
  print(f'Para um valor inicial de R$ {valor_inicial} e uma taxa de juros anual de {taxa_juros_anual}, em {anos} anos você terá R$ {valor_final}') 
  return valor_final

valor_inicial, taxa_juros_anual, anos = 1000.00, 0.05, 10
valor_final = juros_compostos_anual(valor_inicial=valor_inicial, taxa_juros_anual=taxa_juros_anual, anos=anos)

valor_inicial, taxa_juros_anual, anos = 1020.00, 0.03, 10
valor_final = juros_compostos_anual(valor_inicial=valor_inicial, taxa_juros_anual=taxa_juros_anual, anos=anos) 