from flask import *

from forms import *

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


@app.route('/login', methods=['get', 'post'])
def login():
    form_criar_conta = FormCriarConta()
    form_login = FormLogin()

    if form_login.validate_on_submit() and 'btn_submit_login' in request.form:
        # login executado com sucesso
        flash(f"Login feito com sucesso no e-mail {form_login.email.data}", 'alert-success')
        return redirect(url_for('home'))

    if form_criar_conta.validate_on_submit() and 'btn_submit_criar_conta' in request.form:
        # criação da conta bem sucedida
        flash(f"Conta criada com sucesso, bem vindo {form_criar_conta.username.data}",
              'alert-success')  # exibe uma mensagem na tela
        return redirect(url_for('home'))

    return render_template('login.html', form_login=form_login, form_criar_conta=form_criar_conta)


# PRÓXIMA AULA: 598

if __name__ == '__main__':
    app.run(debug=True)
