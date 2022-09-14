from flask import Blueprint, render_template, request, redirect, url_for, flash
from dotenv import load_dotenv
import os
import psycopg2
import psycopg2.extras

load_dotenv()

app_funcionario = Blueprint('app_funcionario', __name__)
conn = psycopg2.connect(
            host= os.getenv("HOST"),
            database= os.getenv("DATABASE"),
            user= os.getenv("USER"),
            password= os.getenv("PASSWORD")
        )

@app_funcionario.route('/funcionario-all')
def funcionario_all():
    funcionario = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    funcionario.execute('SELECT * FROM funcionario')
    funcionarios = funcionario.fetchall()
    return render_template('funcionario/ficha_funcionario.html', funcionarios=funcionarios)


@app_funcionario.route('/funcionario-add', methods=['POST'])
def funcionario_add():
    funcionario = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        codigo = request.form['codigo']
        nome = request.form['nome']
        especialidade = request.form['especialidade']
        cpf = request.form['cpf']
        rg = request.form['rg']
        telefone = request.form['telefone']
        data_adimissao = request.form['data_adimissao']
        salario = request.form['salario']
        foto = request.form['foto']
        funcionario.execute('INSERT INTO funcionario(codigo, nome, especialidade, cpf, rg, telefone, data_adimissao, salario, foto) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)', (codigo, nome, especialidade, cpf, rg, telefone, data_adimissao, salario, foto))
        conn.commit()
        flash('Funcionário adicionado com sucesso!')
        return redirect(url_for('app_funcionario.funcionario_all'))


@app_funcionario.route('/funcionario-edit/<id>', methods=['POST', 'GET'])
def funcionario_edit(id):
    funcionario = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    funcionario.execute('SELECT * FROM funcionario WHERE id = {}'.format(id))
    data = funcionario.fetchall()
    funcionario.close()
    return render_template('funcionario/ficha_funcionario.html', func = data[0])


@app_funcionario.route('/funcionario-update/<id>', methods=['POST'])
def funcionario_update(id):
    if request.method == 'POST':
        codigo = request.form['codigo']
        nome = request.form['nome']
        especialidade = request.form['especialidade']
        cpf = request.form['cpf']
        rg = request.form['rg']
        telefone = request.form['telefone']
        data_adimissao = request.form['data_adimissao']
        salario = request.form['salario']
        foto = request.form['foto']
        funcionario = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        funcionario.execute('UPDATE funcionario SET codigo = %s, nome = %s, especialidade = %s, cpf = %s, rg = %s, telefone = %s, data_adimissao = %s, salario = %s, foto = %s WHERE id = %s', (codigo, nome, especialidade, cpf, rg, telefone, data_adimissao, salario, foto, id))
        flash('Funcionário atualizado com sucesso!')
        conn.commit()
        return redirect(url_for('app_funcionario.funcionario_all'))


@app_funcionario.route('/funcionario-delete/<id>', methods=['POST', 'GET'])
def funcionario_delete(id):
    funcionario = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    funcionario.execute('DELETE FROM funcionario WHERE id = {}'.format(id))
    conn.commit()
    flash('Funcionário removido com sucesso!')
    return redirect(url_for('app_funcionario.funcionario_all'))