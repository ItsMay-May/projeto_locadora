from persistencia import salvar_jogos
jogos = []

def add_jogos():
     
     titulo = input("Título do jogo: ")
     ano_lancamento = input("Ano de lançamento: " )
     valor = float(input('Valor da diaria R$: '))
     plataforma = input("Plataforma: ")
    
     jogo = {  "titulo": titulo, "ano_lancamento": ano_lancamento,"valor": valor,'plataforma':plataforma ,'genero': [] } 
     jogos.append(jogo)
     salvar_jogos(jogos)

def listar_jogos():
     for indice, jogo in enumerate(jogos, start=1):
          print(indice, jogo['titulo'], jogo['valor'])
