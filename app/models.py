from app import db

class Contato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=True)
    email = db.Column(db.String, nullable=True)
    #senha = db.Colunm()

class Livro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=True)
    numero_paginas = db.Column(db.Integer, nullable=True)
    editora = db.Column(db.String, nullable=True)