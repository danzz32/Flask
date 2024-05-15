from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = '5d7f8e99578556d1dcb8c208593b7550'

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


@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
