from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email
from app.models import Contato, db

class ContatoForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    nome =  StringField('Nome', validators=[DataRequired()])
    btnSubmit = SubmitField('Enviar')

    def save(self):
        contato = Contato (
            nome = self.nome.data,
            email = self.email.data
        )
        db.session.add(contato)
        db.session.commit()

class LivroForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    numero_paginas = IntegerField('Número Páginas', validators=[DataRequired()])
    editora = StringField('Editora', validators=[DataRequired()])
    btnSubmit = SubmitField('Enviar')