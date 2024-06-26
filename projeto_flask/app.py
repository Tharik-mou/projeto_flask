from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def obter_produtos():
    with open("produtos.csv", "r") as file:
        lista_produtos = []
        for linha in file:
            nome, descricao, imagem, preco = linha.strip().split(",")

            produto = {
            "nome": nome,
            "descricao": descricao,
            "imagem": imagem,
            "preco": preco
            }

            lista_produtos.append(produto)

        return lista_produtos

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/contato")
def contato():
    return "<h1>Eu amo abacate</h1>"


@app.route("/produtos")
def produtos():
    return render_template("produtos.html", produtos=obter_produtos())


@app.route("/produtos/<nome>")
def produto(nome):
    for produto in obter_produtos():
        if produto['nome'] == nome:
            return render_template("produto.html", produto=produto)
        
    return "O produto não existe!"


@app.route("/produtos/cadastro")
def cadastro_produto():
    return render_template("cadastro_produto.html")

@app.route("/produtos", methods=["POST"])
def salvar_produto():
    nome = request.form['nome']
    descricao = request.form['descricao']
    imagem = request.form['imagem']
    preco = request.form['preco']
    produto = { "nome": nome, "descricao": descricao, "imagem": imagem , "preco": preco}
    adicionar_produtos(produto)
    return redirect(url_for("produtos"))

def adicionar_produtos(produto):
    with open("produtos.csv", "a") as file:
        linha = f"{produto['nome']},{produto['descricao']},{produto['imagem']},{produto['preco']}\n"
        file.write(linha)

app.run(port=5001)