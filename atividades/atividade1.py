from flask import Flask, render_template
import random
from validate_docbr import CPF, CNPJ

cpf = CPF()
cnpj = CNPJ()

app = Flask(__name__)

@app.route("/geradordecpf")
def gerador_de_cpf():
    cpf_do_usuario = cpf.generate(True)
    return render_template("gerador_de_cpf.html", cpf = cpf_do_usuario)

@app.route("/geradordecnpj")
def gerador_de_cnpj():
    cnpj_do_usuario = cnpj.generate(True)
    return render_template("gerador_de_cnpj.html", cnpj = cnpj_do_usuario)

@app.route("/validacaodecpf")
def validacao_de_cpf():
    return render_template("validacao_de_cpf.html")

@app.route("/validacaodecnpj")
def validacao_de_cnpj():
    return render_template("validacao_de_cnpj.html")

app.run()
