from persistencia import registro_locacoes
from jogos import jogos


locacoes = []


def add_locacoes(jogo):
    valor = jogos['valor']
    dias = jogos['dias']
    total = (valor * dias)
    desconto = 0

    if dias > 7:
        desconto = valor * 0.1
    elif dias > 3:
        desconto = valor * 0.05

        
    locacao = {'jogo': jogo, 'dias': dias, 'total': (total - desconto)}
    locacoes.append(locacao)
    registro_locacoes(locacoes)

