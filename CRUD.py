# nome = ["teste1", "teste2", "teste3"]
# idgames = ["teste1", "teste2", "teste3"]
# tamanho = ["teste1", "teste2", "teste3"]
# tipo = ["teste1", "teste2", "teste3"]
# descrição = ["teste1", "teste2", "teste3"]
# games = [nome, idgames, tamanho, tipo, descrição]
#

games = []
 
 
def listarGames():
    print("==== LISTA DE GAMES ====")
    if games:
        for game in range(len(games)):
            print(f"{game} - {games[game]['nome']} | "
                  f"Gênero: {games[game]['genero']} | "
                  f"Plataforma: {games[game]['plataforma']}")
    else:
        print("Nenhum game cadastrado.")
    input("Pressione ENTER para continuar...")
 
 
def adicionarGame():
    print("==== ADICIONAR GAME ====")
    continuar = "s"
    while continuar == "s":
        nome = input("Digite o nome do game: ")
        genero = input("Digite o gênero do game: ")
        plataforma = input("Digite a plataforma do game: ")
 
        # Dicionário representando um único game
        game = {
            "nome": nome,
            "genero": genero,
            "plataforma": plataforma
        }
 
        confirmar = input(f"Tem certeza que deseja adicionar '{nome}'? (s/n): ")
        if confirmar.lower() == "s":
            games.append(game)
            print("Game adicionado com sucesso!")
        else:
            print("Game NÃO adicionado!")
        continuar = input("\nDeseja adicionar mais um game? (s/n): ")
    input("Pressione ENTER para continuar...")
 
 
def buscarGame():
    print("==== BUSCAR GAME ====")
    if games:
        gameEncontrado = False
        posicaoGame = 0
        itemBuscado = input("Digite o nome do game: ")
        for game in range(len(games)):
            if itemBuscado == games[game]["nome"]:
                gameEncontrado = True
                posicaoGame = game
                break
        if gameEncontrado:
            print("Game encontrado!")
            print(f"{posicaoGame} - {games[posicaoGame]['nome']} | "
                  f"Gênero: {games[posicaoGame]['genero']} | "
                  f"Plataforma: {games[posicaoGame]['plataforma']}")
        else:
            print("Game não encontrado!")
    else:
        print("Nenhum game cadastrado.")
    input("Pressione ENTER para continuar...")
 
 
def atualizarGame():
    print("==== ATUALIZAR GAME ====")
    if games:
        gameEncontrado = False
        posicaoGame = 0
        itemBuscado = input("Digite o nome do game: ")
        for game in range(len(games)):
            if itemBuscado == games[game]["nome"]:
                gameEncontrado = True
                posicaoGame = game
                break
        if gameEncontrado:
            novoNome = input("Novo nome do game: ")
            novoGenero = input("Novo gênero do game: ")
            novaPlataforma = input("Nova plataforma do game: ")
            desejaAtualizar = input("\nDeseja fazer a atualização? (s/n): ")
            if desejaAtualizar.lower() == "s":
                confirmar = input(f"\nTem certeza que deseja atualizar '{games[posicaoGame]['nome']}'? (s/n):")
                if confirmar.lower() == "s":
                    games[posicaoGame]["nome"] = novoNome
                    games[posicaoGame]["genero"] = novoGenero
                    games[posicaoGame]["plataforma"] = novaPlataforma
                    print("Game atualizado com sucesso!")
                else:
                    print("Game NÃO atualizado!")
            else:
                print("Game NÃO atualizado!")
        else:
            print("Game não encontrado!")
    else:
        print("Nenhum game cadastrado.")
    input("Pressione ENTER para continuar...")
 
 
def removerGame():
    print("==== REMOVER GAME ====")
    if games:
        gameEncontrado = False
        posicaoGame = 0
        itemBuscado = input("Digite o nome do game: ")
        for game in range(len(games)):
            if itemBuscado == games[game]["nome"]:
                gameEncontrado = True
                posicaoGame = game
                break
        if gameEncontrado:
            confirmar = input(f"Deseja remover '{games[posicaoGame]['nome']}'? (s/n): ")
            if confirmar.lower() == "s":
                games.pop(posicaoGame)
                print("Game removido com sucesso!")
            else:
                print("Remoção cancelada!")
        else:
            print("Game não encontrado!")
    else:
        print("Nenhum game cadastrado.")
    input("Pressione ENTER para continuar...")
 
 
def menu():
    while True:
        print("=====================================")
        print("======== SISTEMA DE GAMES ===========")
        print("====   Versão do Projeto: 0.7    ====")
        print("=====================================")
        print("==== 1 - Listar games            ====")
        print("==== 2 - Adicionar game          ====")
        print("==== 3 - Buscar game             ====")
        print("==== 4 - Atualizar game          ====")
        print("==== 5 - Remover game            ====")
        print("==== 0 - Sair                    ====")
        print("====  Feito por: Wesley V. S. R  ====")
        print("=====================================")
 
        opcao = input("Escolha uma opção: ")
        match opcao:
            case "1":
                listarGames()
            case "2":
                adicionarGame()
            case "3":
                buscarGame()
            case "4":
                atualizarGame()
            case "5":
                removerGame()
            case "0":
                print("Sistema encerrado.")
                break
            case _:
                print("Opção inválida!")
                input("Pressione ENTER para continuar...")
 