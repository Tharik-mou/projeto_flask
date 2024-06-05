from flask import Flask, render_template

lista_produtos = [
    {"nome": "Coca-Cola", "descricao": "veneno"},
    {"nome": "Doritos", "descricao": "suja mão"},
    {"nome": "Agua", "descricao": "limpa mão"},
]

app = Flask(__name__)

@app.route("/")
def home():
    return "<a style='color:black; text-decoration: none;' href='/contato'><h1>Home</h1></a>"


@app.route("/contato")
def contato():
    return "<h1>Eu amo abacate</h1>"


@app.route("/produtos")
def produtos():
    return render_template("produtos.html", produtos = lista_produtos)


@app.route("/produtos/<nome>")
def produto(nome):
    for produto in lista_produtos:
        if produto['nome'] == nome:
            return f"{produto['nome']}, {produto['descricao']}"
        
    return "O produto não existe!"