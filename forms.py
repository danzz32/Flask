from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *


# CLASSE PARA O FORM DE CRIAR CONTA
class FormCriarConta(FlaskForm):
    username = StringField('Nome de usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(8, 16)])
    confirmacao_senha = PasswordField('Confirmação da senha', validators=[DataRequired(), EqualTo('senha')])
    btn_submit = SubmitField('Criar Conta')


# CLASSE PARA O FORM DE LOGIN
class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(8, 16)])
    btn_submit = SubmitField('Fazer login')
