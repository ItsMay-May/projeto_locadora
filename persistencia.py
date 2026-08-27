import json

def salvar_jogos(add_jogos):
    with open ('jogos.json' , 'w' , encoding="utf-8") as arquivo:
        json.dump(add_jogos, arquivo, ensure_ascii=False, indent=4 )


def carregar_jogos():
    try:
        with open ('clientes.json', 'r', encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []


def salvar_clientes(cadastro_clientes):
    with open('clientes.json', 'w', encoding="utf-8") as arquivo:
        json.dump(cadastro_clientes, arquivo, indent=4)

def carregar_clientes():
    try:
        with open('clientes,json' , 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
    

def registro_locacoes(add_locacoes):
    with open('locacoes.json', 'w', encoding="utf-8") as arquivo:
        json.dump(add_locacoes, arquivo, indent=4)


def carregar_locacoes():
    try:
        with open('locacoes.json', 'r', encoding="utf-8")as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []