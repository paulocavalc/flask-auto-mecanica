from flask import Blueprint, render_template, request, redirect, url_for, flash
from dotenv import load_dotenv
import os
import psycopg2
import psycopg2.extras

load_dotenv()

app_empresa = Blueprint('app_empresa', __name__)
conn = psycopg2.connect(
            host= os.getenv("HOST"),
            database= os.getenv("DATABASE"),
            user= os.getenv("USER"),
            password= os.getenv("PASSWORD")
        )

@app_empresa.route('/empresa-all')
def empresa_all():
    empresa = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    empresa.execute('SELECT * FROM empresa')
    empresas = empresa.fetchall()
    return render_template('empresa/ficha_empresa.html', empresas=empresas)


@app_empresa.route('/empresa-add', methods=['POST'])
def empresa_add():
    empresa = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        cnpj = request.form['cnpj']
        nome = request.form['nome']
        inscricao_estadual = request.form['inscricao_estadual']
        endereco = request.form['endereco']
        latitude = request.form['latitude']
        longitude = request.form['longitude']
        empresa.execute('INSERT INTO empresa(cnpj, nome, inscricao_estadual, endereco, latitude, longitude) VALUES(%s, %s, %s, %s, %s, %s)', (cnpj, nome, inscricao_estadual, endereco, latitude, longitude))
        conn.commit()
        flash('Empresa adicionado com sucesso!')
        return redirect(url_for('app_empresa.empresa_all'))


@app_empresa.route('/empresa-edit/<id>', methods=['POST', 'GET'])
def empresa_edit(id):
    empresa = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    empresa.execute('SELECT * FROM empresa WHERE id = {}'.format(id))
    data = empresa.fetchall()
    empresa.close()
    return render_template('empresa/ficha_empresa.html', emp = data[0])


@app_empresa.route('/empresa-update/<id>', methods=['POST'])
def empresa_update(id):
    if request.method == 'POST':
        cnpj = request.form['cnpj']
        nome = request.form['nome']
        inscricao_estadual = request.form['inscricao_estadual']
        endereco = request.form['endereco']
        latitude = request.form['latitude']
        longitude = request.form['longitude']
        empresa = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        empresa.execute('UPDATE empresa SET cnpj = %s, nome = %s, inscricao_estadual = %s, endereco = %s, latitude = %s, longitude = %s WHERE id = %s', (cnpj, nome, inscricao_estadual, endereco, latitude, longitude, id))
        flash('Empresa atualizado com sucesso!')
        conn.commit()
        return redirect(url_for('app_empresa.empresa_all'))


@app_empresa.route('/empresa-delete/<id>', methods=['POST', 'GET'])
def empresa_delete(id):
    empresa = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    empresa.execute('DELETE FROM empresa WHERE id = {}'.format(id))
    conn.commit()
    flash('Empresa removido com sucesso!')
    return redirect(url_for('app_empresa.empresa_all'))
