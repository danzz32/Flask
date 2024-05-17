from datetime import datetime

from comunidadeimpressionadora import database


class Usuario(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(100), nullable=False)
    email = database.Column(database.String(100), nullable=False, unique=True)
    senha = database.Column(database.String(16), nullable=False)
    foto_perfil = database.Column(database.String, default='default.png')
    posts = database.relationship('Post', backref='autor', lazy=True)
    cursos = database.Column(database.String, nullable=False, default='Não Informado')


class Post(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    titulo = database.Column(database.String(100), nullable=False)
    conteudo = database.Column(database.Text, nullable=False)
    data_criacao = database.Column(
        database.DateTime,
        nullable=False,
        default=datetime.utcnow
    )
    usuario_id = database.Column(
        database.Integer,
        database.ForeignKey('usuario.id'),
        nullable=False
    )
