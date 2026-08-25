from persistencia import cadastro_clientes

clientes = []

def cadastro_clientes(nome, data_nascimento, cpf,):
    
    nome = input("Nome do cliente: ")
    data_nascimento = input("Data de nascimento: ")
    cpf = input("Seu CPF: ")

    cliente = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf
    }

    clientes.append(cliente)
    cadastro_clientes(clientes)