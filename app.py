# """
# app.py - Catálogo de Games (versão Web com Flask)

# Este arquivo é a evolução do CRUD.py original (feito para terminal).
# Todas as 5 operações do projeto original foram mantidas:
#     1 - Listar games   -> rota "/"
#     2 - Adicionar game -> rota "/adicionar"
#     3 - Buscar game    -> rota "/buscar"
#     4 - Atualizar game -> rota "/atualizar/<indice>"
#     5 - Remover game   -> rota "/remover/<indice>"

# A diferença é que, em vez de usar a lista "games" apenas em memória
# (como no terminal), agora ela é persistida em disco no arquivo
# games.json, usando a biblioteca "json" nativa do Python, conforme
# o material do professor (Arquivos e Arquivos JSON).
# """

import json
import os
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

# Necessário para o uso de flash() (mensagens de sucesso/erro na tela)
app.secret_key = "chave-secreta-ifba-gamesoline"

# Caminho do "banco de dados" em JSON
ARQUIVO_JSON = "games.json"


# ============================================================
# FUNÇÕES DE APOIO -> manipulação do arquivo JSON
# (equivalente ao que os PDFs "Arquivos" e "Arquivos JSON" ensinam)
# ============================================================

def carregar_games():
    # """
    # Lê o arquivo games.json e devolve a lista de dicionários de games.
    # Usa o gerenciador de contexto "with open(...)" no modo "r" (leitura),
    # com encoding="utf-8" para lidar corretamente com acentos.
    # """
    if not os.path.exists(ARQUIVO_JSON):
        # Se o arquivo ainda não existe, começamos com uma lista vazia
        return []

    with open(ARQUIVO_JSON, "r", encoding="utf-8") as arquivo:
        try:
            # json.load() lê o conteúdo do arquivo e converte para
            # estruturas Python (lista de dicionários, nesse caso)
            return json.load(arquivo)
        except json.JSONDecodeError:
            # Se o arquivo estiver vazio ou corrompido, evita quebrar a aplicação
            return []


def salvar_games(games):
    """
    Recebe a lista de games e grava no arquivo games.json.
    Usa o modo "w" (escrita), que substitui o conteúdo existente,
    também com encoding="utf-8".
    """
    with open(ARQUIVO_JSON, "w", encoding="utf-8") as arquivo:
        # json.dump() converte a lista/dicionário Python para o formato JSON
        # indent=4        -> deixa o arquivo .json formatado e legível
        # ensure_ascii=False -> preserva acentos (ã, ç, é...) em vez de \uXXXX
        json.dump(games, arquivo, indent=4, ensure_ascii=False)


# ============================================================
# ROTAS DA APLICAÇÃO (equivalentes às funções do CRUD.py)
# ============================================================

@app.route("/")
def listar_games():
    """Equivalente a listarGames() do CRUD.py original."""
    games = carregar_games()
    return render_template("index.html", games=games)


@app.route("/adicionar", methods=["GET", "POST"])
def adicionar_game():
    """Equivalente a adicionarGame() do CRUD.py original."""
    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        genero = request.form.get("genero", "").strip()
        plataforma = request.form.get("plataforma", "").strip()

        if nome and genero and plataforma:
            games = carregar_games()

            # Mesmo dicionário usado no CRUD.py original
            novo_game = {
                "nome": nome,
                "genero": genero,
                "plataforma": plataforma,
            }

            games.append(novo_game)
            salvar_games(games)

            flash(f"Game '{nome}' adicionado com sucesso!", "sucesso")
            return redirect(url_for("listar_games"))
        else:
            flash("Preencha todos os campos antes de salvar!", "erro")

    return render_template("adicionar.html")


@app.route("/buscar", methods=["GET"])
def buscar_game():
    """
    Equivalente a buscarGame() do CRUD.py original,
    mas agora com busca PARCIAL (não precisa digitar o nome todo)
    e retornando TODOS os games que combinam com o termo digitado.
    """
    termo = request.args.get("termo", "").strip()
    resultados = []  # lista de tuplas (indice_original, game)

    if termo:
        games = carregar_games()
        for indice, game in enumerate(games):
            # "in" verifica se o termo está CONTIDO no nome (busca parcial)
            # .lower() nos dois lados torna a busca sem distinção de maiúsc./minúsc.
            if termo.lower() in game["nome"].lower():
                resultados.append((indice, game))

    return render_template("buscar.html", resultados=resultados, termo=termo)


@app.route("/atualizar/<int:indice>", methods=["GET", "POST"])
def atualizar_game(indice):
    """Equivalente a atualizarGame() do CRUD.py original."""
    games = carregar_games()

    # Verifica se o índice recebido pela URL realmente existe na lista
    if indice < 0 or indice >= len(games):
        flash("Game não encontrado!", "erro")
        return redirect(url_for("listar_games"))

    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        genero = request.form.get("genero", "").strip()
        plataforma = request.form.get("plataforma", "").strip()

        if nome and genero and plataforma:
            games[indice] = {
                "nome": nome,
                "genero": genero,
                "plataforma": plataforma,
            }
            salvar_games(games)

            flash("Game atualizado com sucesso!", "sucesso")
            return redirect(url_for("listar_games"))
        else:
            flash("Preencha todos os campos antes de atualizar!", "erro")

    # GET: mostra o formulário já preenchido com os dados atuais do game
    return render_template("atualizar.html", game=games[indice], indice=indice)


@app.route("/remover/<int:indice>", methods=["POST"])
def remover_game(indice):
    """Equivalente a removerGame() do CRUD.py original."""
    games = carregar_games()

    if 0 <= indice < len(games):
        removido = games.pop(indice)
        salvar_games(games)
        flash(f"Game '{removido['nome']}' removido com sucesso!", "sucesso")
    else:
        flash("Game não encontrado!", "erro")

    return redirect(url_for("listar_games"))


# ============================================================
# EXECUÇÃO DA APLICAÇÃO
# ============================================================

if __name__ == "__main__":
    # debug=True facilita o desenvolvimento (recarrega o servidor sozinho
    # e mostra mensagens de erro detalhadas). Em produção, isso deve ser False.
    app.run(debug=True)
