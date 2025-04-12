#são do tipo dict, armazenam sqquencias chave-valor, não é perminito chaves duplicadas, podemos criar dicionarios compostos.

carro = {
    'marca': 'Volkswagen',
    'modelo': 'Polo',
    'ano': 2021,
    'ano': 2004
}

print(carro)


cadastro = {
    'andre': {
        'nome': 'Andre Perez',
        'ano_nascimento': 1992,
        'pais': {
            'pai': {
              'nome': '<nome-do-pai> Perez',
              'ano_nascimento': 1971
            },
            'mae': {
              'nome': '<nome-da-mae> Perez',
              'ano_nascimento': 1973
            },
        }
    }
}

print(cadastro)

cadastro['andre']['pais']['mae']['ano_nascimento']