#Você trabalha como analista de dados de mídias sociais e precisa descobrir todas as hashtags que alcançaram o top trending do Twitter durante uma semana. Você já conseguiu as hashtags por dia da semana:

hashtags_seg = ['#tiago', '#joao', '#bbb']
hashtags_ter = ['#sarah', '#bbb', '#fiuk']
hashtags_qua = ['#gil', '#thelma', '#lourdes']
hashtags_qui = ['#rafa', '#fora', '#danilo']
hashtags_sex = ['#juliete', '#arthur', '#bbb']

hashtags_semana = hashtags_seg + hashtags_ter + hashtags_qua + hashtags_qui + hashtags_sex
print(hashtags_semana)


#melhorando o codigo
print(hashtags_semana)
print(len(hashtags_semana))

hashtags_semana = list(set(hashtags_seg + hashtags_ter + hashtags_qua + hashtags_qui + hashtags_sex))

print(hashtags_semana)
print(len(hashtags_semana))
