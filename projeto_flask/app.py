from flask import Flask, render_template, request, redirect, url_for

lista_produtos = [
    {"nome": "Coca-Cola", "descricao": "veneno"},
    {"nome": "Doritos", "descricao": "suja mão"},
    {"nome": "Agua", "descricao": "limpa mão"},
]

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/contato")
def contato():
    return "<h1>Eu amo abacate</h1>"


@app.route("/produtos")
def produtos():
    return render_template("produtos.html", produtos=lista_produtos)


@app.route("/produtos/<nome>")
def produto(nome):
    for produto in lista_produtos:
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
    produto = { "nome": nome, "descricao": descricao }
    lista_produtos.append(produto)
    return redirect(url_for("produtos"))

app.run(port=5001)