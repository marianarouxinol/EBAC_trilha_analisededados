juros = [0.05, 0.07, 0.02, 0.04, 0.08]
print(juros)
print(type(juros))


#inserir elemento sem substituir, insert, pode escolher a posição, no exemplo abaixo escolhi a psução 0

juros.insert(0,0.10)
print(juros)


#append, adiciona no final da lista

juros.append(0.09)
print(juros)

#remover um elemento pelo valor, remove

juros.remove(0.1)
print(juros)

#remover um valor pelo índice, pop

terceiro_juros=juros.pop(2)
print(terceiro_juros)