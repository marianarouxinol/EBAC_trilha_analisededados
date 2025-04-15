def escreve_arquivo_csv(nome: str, cabecalho: str, conteudos: list) -> bool:

  try: 

    with open(file=nome, mode='w', encoding='utf8') as fp:
      linha = cabecalho + '\n'
      fp.write(linha)
      for conteudo in conteudos:
        linha = str(conteudo) + '\n'
        fp.write(linha)

  except Exception as exc:
    
    print(exc)
    return False

  return True

nome = 'idades-funcao-erro.csv'
cabecalho = 'idade' 
conteudos = [30, 33, 35, 30, 59, 35, 36, 39, 41, 43]

escreveu_com_sucesso = escreve_arquivo_csv(nome=nome, cabecalho=cabecalho, conteudos=conteudos)
print(escreveu_com_sucesso)