from app import app
from flask import render_template, url_for, request, redirect
from app.forms import ContatoForm, LivroForm
from app.models import Contato, db, Livro
@app.route('/')
def pagina_inicial():
    nome = "Pedro"
    return render_template('index.html', nome=nome)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    form = LivroForm()
    context = {}
    if form.validate_on_submit():
        form.save()
        return redirect(url_for('pagina_inicial'))
    return render_template('cadastro.html', context=context, form=form)

@app.route('/cadastro/usuario', methods=['GET', 'POST'])
def cadastro_usuario():
    form = ContatoForm()
    context = {}
    if form.validate_on_submit():
        form.save()
        return redirect(url_for('pagina_inicial'))
    return render_template('cadastro_pessoa.html', context=context, form=form)