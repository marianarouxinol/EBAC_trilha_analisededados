anos = [2019, 2020, 2021]

try:
  ano_atual = anos[3]
  print(ano_atual)
except Exception as exc:
  print('Descrição da exceção: ' + str(exc))
  print('Tipo da exceção: ' + str(type(exc)))
  print('Lista de anos é menor que o valor escolhido. Espera-se um valor entre 0 e ' + str(len(anos) - 1))