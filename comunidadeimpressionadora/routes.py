from comunidadeimpressionadora import *
from comunidadeimpressionadora.forms import FormCriarConta, FormLogin
from comunidadeimpressionadora.models import *

lista_usuarios = []


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/contatos')
def contato():
    return render_template("contatos.html")


@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form_criar_conta = FormCriarConta()
    form_login = FormLogin()

    if form_login.validate_on_submit() and 'btn_submit_login' in request.form:
        # login executado com sucesso
        flash(f"Login feito com sucesso no e-mail {form_login.email.data}",
              'alert-success')
        return redirect(url_for('home'))

    if form_criar_conta.validate_on_submit() and 'btn_submit_criar_conta' in request.form:
        # criar o usuário
        usuario = Usuario(
            username={form_criar_conta.username.data},
            email={form_criar_conta.email.data},
            senha={form_criar_conta.senha.data},
            foto_perfil='default.png',
            cursos='Não informado'
        )
        # inserindo no banco de dados
        database.session.add(usuario)
        database.session.commit()
        # criação da conta bem sucedida
        flash(
            f"Conta criada com sucesso, bem vindo {form_criar_conta.username.data}",
            'alert-success')  # exibe uma mensagem na tela
        return redirect(url_for('home'))

    return render_template('login.html', form_login=form_login,
                           form_criar_conta=form_criar_conta)
