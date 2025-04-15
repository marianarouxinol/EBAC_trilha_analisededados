nome = 'Andre Perez'
idade = 19

try:
  apresentacao = 'Fala pessoal, meu nome é ' + nome + ' e eu tenho ' + idade + ' anos'
  print(apresentacao)
except TypeError:
  idade = str(idade)
finally:
  print('Segunda chance')
  apresentacao = 'Fala pessoal, meu nome é ' + nome + ' e eu tenho ' + idade + ' anos'
  print(apresentacao)