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