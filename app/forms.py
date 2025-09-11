from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email
from app.models import Contato, db

class ContatoForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    nome =  StringField('Nome', validators=[DataRequired()])
    btnSubmit = SubmitField('Enviar')

    def save(self):
        contato = Contato (
            nome = self.nome.data,
            email = self.email.data
        )
        db.session.add(contato)
        db.session.commit()