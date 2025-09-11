from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

class ContatoForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    nome =  StringField('Nome', validators=[DataRequired()])