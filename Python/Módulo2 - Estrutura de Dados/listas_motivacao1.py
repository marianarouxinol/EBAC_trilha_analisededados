#O aplicativo do seu banco registra toda a sua movimentação financeira. No final do dia, o app consolida o saldo final para que você possa controlar sua vida financeira

dia_11_saldo_inicial = 1000

dia_11_transacao_1 = 243
dia_11_transacao_2 = -798.58
dia_11_transacao_3 = 427.12
dia_11_transacao_4 = -10.91

dia_11_saldo_final = dia_11_saldo_inicial + dia_11_transacao_1 + dia_11_transacao_2 + dia_11_transacao_3 + dia_11_transacao_4
print(dia_11_saldo_final)

#Será que exista uma forma melhor de armazenar as transações diárias?

#resposta

dia_11_saldo_inicial = 1000
dia_11_transacoes = []

dia_11_transacoes.append(243)
dia_11_transacoes.append(-798.58)
dia_11_transacoes.append(427.12)
dia_11_transacoes.append(-10.91)

print(dia_11_transacoes)

dia_11_saldo_final = dia_11_saldo_inicial + dia_11_transacoes[0] + dia_11_transacoes[1] + dia_11_transacoes[2] + dia_11_transacoes[3]
print(dia_11_saldo_final)