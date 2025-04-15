codigo_de_seguranca = '802'
codigo_de_seguranca_cadastro = '852'

senha = '7703'
senha_cadastro = '7783'

if (codigo_de_seguranca == codigo_de_seguranca_cadastro) & (senha == senha_cadastro):
  print("Pagamento efetuado")

elif (codigo_de_seguranca != codigo_de_seguranca_cadastro) & (senha == senha_cadastro):
  print("Erro: Código de segurança inválido")

elif (codigo_de_seguranca == codigo_de_seguranca_cadastro) & (senha != senha_cadastro):
  print("Erro: Senha inválida inválida")

else:
  print("Erro: Código de segurança e senha inválidos")