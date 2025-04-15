import csv

idades = []

with open(file='./dados.csv', mode='r', encoding='utf8') as arquivo:
    linha = arquivo.readline()  
    
    linha = arquivo.readline() 
    while linha:
        linha_separada = linha.strip().split(',')  
        
        try:
            idade = int(linha_separada[1]) 
            idades.append(idade)  
        except ValueError:
            print(f"Erro ao converter a idade: {linha_separada}") 
            
        linha = arquivo.readline()

print(idades)


with open(file='idades.csv', mode='w', encoding='utf8') as fp:
  linha = 'idade' + '\n'
  fp.write(linha)
  for idade in idades:
    linha = str(idade) + '\n'
    fp.write(linha)

with open(file='idades.csv', mode='a', encoding='utf8') as fp:
  for idade in idades:
    linha = str(idade + 100) + '\n'
    fp.write(linha)