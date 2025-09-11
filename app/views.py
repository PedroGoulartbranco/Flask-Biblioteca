from app import app
from flask import render_template, url_for, request
from app.forms import ContatoForm
@app.route('/')
def pagina_inicial():
    nome = "Pedro"
    return render_template('index.html', nome=nome)

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/cadastro/usuario', methods=['GET', 'POST'])
def cadastro_usuario():
    context = {}
    if request.method == 'POST':
        email = request.form['email']
        context.update({'email': email})
        print(email)
    return render_template('cadastro_pessoa.html', context=context)