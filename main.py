from flask import Flask, render_template, url_for

app = Flask(__name__)

lista_usuarios = ['Danilo', 'Daniel', 'Thayla', 'Clelton', 'Ericles']


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/contatos')
def contato():
    return render_template("contatos.html")


@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)


if __name__ == '__main__':
    app.run(debug=True)
