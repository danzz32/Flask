from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/contatos')
def contato():
    return 'Qualquer dúvida consulte um dos contatos abaixo'


if __name__ == '__main__':
    app.run(debug=True)
