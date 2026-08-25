import json

def salvar_jogos(jogos):
    with open ('jogos.json' , 'w' , encoding="utf-8") as arquivo:
        json.dump(jogos, arquivo, ensure_ascii=False, indent=4 )


def carregar_jogos():
    try:
        with open ('clientes.json', 'r', encoding="ut-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []


def cadastro_clientes(clientes):
    with open('clientes.json', 'r', encoding="utf=8") as arquivo:
        json.dump(clientes, arquivo, indent=4)

def carregar_clientes():
    try:
        with open('clientes,json' , 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
    

def registro_locacoes(locacoes):
    with open('locacoes.json', 'w', encoding="utf-8") as arquivo:
        json.dump(locacoes, arquivo, indent=4)


def carregar_locacoes():
    try:
        with open('locacoes.json', 'r', encoding="utf-8")as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []