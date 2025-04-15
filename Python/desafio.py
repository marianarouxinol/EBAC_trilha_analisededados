
quantidade_cds = int(input("Quantos CDs você tem na coleção? "))


valores = []  
total_investido = 0  


for i in range(quantidade_cds):
    valor = float(input(f"Digite o valor pago pelo CD {i+1}: R$ "))
    valores.append(valor)  
    total_investido += valor  


media_gasto = total_investido / quantidade_cds


print("\n📀 Resumo da coleção 📀")
print(f"Total investido: R$ {total_investido:.2f}")
print(f"Média de gasto por CD: R$ {media_gasto:.2f}")