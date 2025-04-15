def extrair_usuario_email_provedor(email: str) -> (str, str):
  email_separado = email.split(sep='@')
  usuario = email_separado[0]
  provedor = email_separado[1]
  return usuario, provedor


email = 'mari.mm@gmail.com'
usuario, provedor = extrair_usuario_email_provedor(email=email)
print(usuario)
print(provedor)