from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy
from app.model.table import Aluno
from app import app,db


def temLetra(string):
    string = string.lower()
    return string.islower()
    

@app.route('/')
def index(methods=['GET','POST']):
    alunos = Aluno.query.all()
    return render_template('index.html', alunos= alunos)

@app.route('/create',methods=['GET','POST','PUT'])
def create():
    alunos = Aluno.query.all()
    aluno = None
    if request.method == 'POST':
        aluno = Aluno(request.form['nome'],
        request.form['email'],
        request.form['numero'],
        request.form['cep'],
        request.form['complemento'])
        a = aluno.getCep()
        if a == False:
            return render_template('create.html',aluno=aluno,alunos=alunos,style='#e92929', initial='initial', visibility='visible')
        db.session.add(aluno)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create.html',alunos=alunos,aluno=aluno)

@app.route('/update/<int:ra>',methods=['GET','POST'])
def update(ra):
    alunos = Aluno.query.all()
    aluno = Aluno.query.get(ra)
    if request.method == 'POST':
        aluno.nome = request.form['nome']
        aluno.email = request.form['email']
        aluno.numero = request.form['numero']
        aluno.cep = request.form['cep']
        a = aluno.getCep()
        if a == False:
            return render_template('update.html', aluno=aluno,style='#e92929',alunos=alunos,visibility='visible')
        aluno.complemento = request.form['complemento']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('update.html', aluno=aluno, alunos=alunos)
        
@app.route('/delete/<int:ra>', methods=['GET','POST'])
def delete(ra):
    aluno = Aluno.query.get(ra)
    db.session.delete(aluno)
    db.session.commit()
    return redirect(url_for('index'))

#falta finalizar a busca
@app.route('/find',methods=['GET','POST'])
def find():
    lista = []
    if request.method == "POST":
        item = request.form['texto']
        i = item.lower()
        alunos = Aluno.query.all()
        for a in alunos:
            if (i in a.nome.lower()) or (i in a.email.lower()) or (i in a.numero.lower()) or (i in a.cep.lower()) or (i in a.complemento.lower()) or (i in a.logradouro.lower()):
                lista.append(a)

        if temLetra(item)==False and item.strip() == False:
            ra = int(item)
            aluno = Aluno.query.get(ra)
            if aluno not in lista: lista.append(aluno)

        return render_template('index.html', alunos= lista,item = item, X='X')
    return render_template('find.html')
