from comunidadeimpressionadora import app
from comunidadeimpressionadora.models import Usuario

with app.app_context():
  # INSERINDO USUÁRIOS DE TESTE NO DB
  # usuario = Usuario()
  # usuario.username = 'Danilo'
  # usuario.email = 'ztejd@example.com'
  # usuario.senha = '123456'
  #
  # usuario2 = Usuario()
  # usuario2.username = 'Daniel'
  # usuario2.email = 'ejeyd@example.com'
  # usuario2.senha = '654321'
  #
  # database.session.add(usuario)
  # database.session.add(usuario2)
  #
  # database.session.commit()

  # TESTES
  # REALIZANDO CONSULTAS
  usuario_test = Usuario.query.filter_by(username='Danilo').first()
  print(usuario_test)
