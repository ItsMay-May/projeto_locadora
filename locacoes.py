from persistencia import registro_locacoes


locacoes = []


def registro_locacoes(jogo, dias):
    valor = jogo['valor']
    dias = jogo['dias']
    total = (valor * dias)
    desconto = 0

    if dias > 7:
        desconto = valor * 0.1
    elif dias > 3:
        desconto = valor * 0.05

        
    locacao = {'jogo': jogo, 'dias': dias, 'total': (total - desconto)}
    locacoes.append(locacao)
    registro_locacoes(locacoes)

