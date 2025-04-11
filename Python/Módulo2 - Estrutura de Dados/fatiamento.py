fabricantes_mobile_china = ['xiaomi', 'huawei']
fabricantes_mobile_eua = ['apple', 'motorola']
fabricantes_mobile = fabricantes_mobile_china + fabricantes_mobile_eua

print(fabricantes_mobile_china)
print(fabricantes_mobile_eua)
print(fabricantes_mobile)
print(f'0: {fabricantes_mobile[0]}') Claro, Mariana! Vamos destrinchar esse código passo a passo.
1️⃣ Definição de listas:
O código começa criando duas listas:
- fabricantes_mobile_china = ['xiaomi', 'huawei'] → Lista com fabricantes chineses.
- fabricantes_mobile_eua = ['apple', 'motorola'] → Lista com fabricantes dos EUA.

2️⃣ União das listas:
A terceira linha do código cria uma nova lista fabricantes_mobile, que une (+) as duas listas anteriores:
fabricantes_mobile = fabricantes_mobile_china + fabricantes_mobile_eua


Isso resulta na lista:
['xiaomi', 'huawei', 'apple', 'motorola']


3️⃣ Impressão das listas:
O código usa print() para exibir cada lista separadamente:
print(fabricantes_mobile_china)  # ['xiaomi', 'huawei']
print(fabricantes_mobile_eua)    # ['apple', 'motorola']
print(fabricantes_mobile)        # ['xiaomi', 'huawei', 'apple', 'motorola']


print(f'0: {fabricantes_mobile[0]}')
print(f'-1: {fabricantes_mobile[-1]}')