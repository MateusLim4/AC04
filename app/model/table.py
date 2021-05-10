from app import db
from requests import api

class Aluno(db.Model):
    ra = db.Column(db.Integer,primary_key=True,autoincrement=True)
    nome = db.Column(db.String(60))
    email = db.Column(db.String(50))
    logradouro = db.Column(db.String(50)) #pegar com o viacep
    numero = db.Column(db.String(20))
    cep = db.Column(db.String(10))
    complemento  = db.Column(db.String(60))

    def __init__(self,nome,email,numero,cep,complemento):
        self.nome = nome
        self.email = email
        self.numero = numero
        self.cep = cep
        self.complemento = complemento
        self.logradouro = None

    def getCep(self):
        url = api.get(f'https://viacep.com.br/ws/{self.cep}/json')
        if url.status_code == 400: 
            return False
        self.logradouro = url.json()['logradouro']
        return True