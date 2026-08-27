from persistencia import registro_locacoes
from jogos import jogos, listar_jogos


locacoes = []


def add_locacoes():
    print("Jogos disponíveis...")
    listar_jogos()
    jogo_escolhido = int(input("Digite o código do jogo escolhido: "))
    jogo = jogos[jogo_escolhido-1]
    valor = jogo['valor']
    dias = int(input("Dias alugados: "))
    total = (valor * dias)
    desconto = 0

    if dias > 7:
        desconto = valor * 0.1
    elif dias > 3:
        desconto = valor * 0.05

        
    locacao = {'jogo': jogos['jogo'], 'dias': dias, 'total': (total - desconto)}
    locacoes.append(locacao)
    registro_locacoes(locacoes)

