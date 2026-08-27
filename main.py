from jogos import (add_jogos)
from locacoes import (add_locacoes)
from clientes import(cadastro_clientes)
from persistencia import(
    carregar_clientes,
    carregar_jogos,
    carregar_locacoes
)

def menu():
    while(True):
        print("---Bem vindo a locadora do Tiago Postgres, escolha uma das opções abaixo:---")
        print("\n1-Cadastrar jogos \n2-Cadastrar novo cliente \n3-Registrar locação \n4-Listar jogos disponíveis \n5- Ver clientes cadastrados \n6-Ver resistros de locações \n7- Sair")
        cod = int(input("Insira aqui: "))

        if cod == 1:
            add_jogos()
        elif cod == 2:
            cadastro_clientes()
        elif cod == 3:
            add_locacoes()
        elif cod == 4:
        
            carregar_jogos()
        elif cod == 5:
            carregar_clientes()
        elif cod == 6:
            carregar_locacoes()
        elif cod == 7:
            print("Saindo ...")
            break
        else:
            print("Número inválido! Tente novamente.")
            continue
menu()