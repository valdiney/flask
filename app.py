from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('views/dashboard/index.html')


@app.route("/sistema_linguagem")
def sistema_de_linguagem():
    return render_template('views/teoria/sistema_de_linguagem.html')


app.run()