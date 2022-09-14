from flask import Blueprint, render_template, request, redirect, url_for, flash
from dotenv import load_dotenv
import os
import psycopg2
import psycopg2.extras

load_dotenv()

app_servico = Blueprint('app_servico', __name__)
conn = psycopg2.connect(
            host= os.getenv("HOST"),
            database= os.getenv("DATABASE"),
            user= os.getenv("USER"),
            password= os.getenv("PASSWORD")
        )

@app_servico.route('/servico-all')
def servico_all():
    servico = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    servico.execute('SELECT * FROM servico')
    servicos = servico.fetchall()
    return render_template('servico/ficha_servico.html', servicos=servicos)


@app_servico.route('/servico-add', methods=['POST'])
def servico_add():
    servico = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        codigo = request.form['codigo']
        descricao = request.form['descricao']
        valor_servico = request.form['valor_servico']
        servico.execute('INSERT INTO servico(codigo, descricao, valor_servico) VALUES(%s, %s, %s)', (codigo, descricao, valor_servico))
        conn.commit()
        flash('Serviço adicionado com sucesso!')
        return redirect(url_for('app_servico.servico_all'))


@app_servico.route('/servico-edit/<id>', methods=['POST', 'GET'])
def servico_edit(id):
    servico = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    servico.execute('SELECT * FROM servico WHERE id = {}'.format(id))
    data = servico.fetchall()
    servico.close()
    return render_template('servico/ficha_servico.html', serv = data[0])


@app_servico.route('/servico-update/<id>', methods=['POST'])
def servico_update(id):
    if request.method == 'POST':
        codigo = request.form['codigo']
        descricao = request.form['descricao']
        valor_servico = request.form['valor_servico']
        servico = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        servico.execute('UPDATE servico SET codigo = %s, descricao = %s, valor_servico = %s WHERE id = %s', (codigo, descricao, valor_servico, id))
        flash('Serviço atualizado com sucesso!')
        conn.commit()
        return redirect(url_for('app_servico.servico_all'))


@app_servico.route('/servico-delete/<id>', methods=['POST', 'GET'])
def servico_delete(id):
    servico = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    servico.execute('DELETE FROM servico WHERE id = {}'.format(id))
    conn.commit()
    flash('Serviço removido com sucesso!')
    return redirect(url_for('app_servico.servico_all'))