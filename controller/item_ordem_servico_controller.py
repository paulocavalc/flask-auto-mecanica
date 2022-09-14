from flask import Blueprint, render_template, request, redirect, url_for, flash
from dotenv import load_dotenv
import os
import psycopg2
import psycopg2.extras

load_dotenv()

app_item_ordem_servico = Blueprint('app_item_ordem_servico', __name__)
conn = psycopg2.connect(
            host= os.getenv("HOST"),
            database= os.getenv("DATABASE"),
            user= os.getenv("USER"),
            password= os.getenv("PASSWORD")
        )

@app_item_ordem_servico.route('/item-ordem-servico-all')
def item_ordem_servico_all():
    item_ordem_servico = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    item_ordem_servico.execute('SELECT * FROM item_ordem_servico')
    itens_ordens_servicos = item_ordem_servico.fetchall()
    return render_template('item_ordem_servico/ficha_item_ordem_servico.html', itens_ordens_servicos=itens_ordens_servicos)


@app_item_ordem_servico.route('/item-ordem-servico-add', methods=['POST'])
def item_ordem_servico_add():
    item_ordem_servico = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        codigo = request.form['codigo']
        codigo_item_servico = request.form['codigo_item_servico']
        codigo_funcionario = request.form['codigo_funcionario']
        codigo_ordem_servico = request.form['codigo_ordem_servico']
        item_ordem_servico.execute('INSERT INTO item_ordem_servico(codigo, codigo_item_servico, codigo_funcionario, codigo_ordem_servico) VALUES(%s, %s, %s, %s)', (codigo, codigo_item_servico, codigo_funcionario, codigo_ordem_servico))
        conn.commit()
        flash('Item Ordem Serviço adicionado com sucesso!')
        return redirect(url_for('app_item_ordem_servico.item_ordem_servico_all'))


@app_item_ordem_servico.route('/item-ordem-servico-edit/<id>', methods=['POST', 'GET'])
def item_ordem_servico_edit(id):
    item_ordem_servico = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    item_ordem_servico.execute('SELECT * FROM item_ordem_servico WHERE id = {}'.format(id))
    data = item_ordem_servico.fetchall()
    item_ordem_servico.close()
    return render_template('item_ordem_servico/ficha_item_ordem_servico.html', orde = data[0])


@app_item_ordem_servico.route('/item-ordem-servico-update/<id>', methods=['POST'])
def item_ordem_servico_update(id):
    if request.method == 'POST':
        codigo = request.form['codigo']
        codigo_item_servico = request.form['codigo_item_servico']
        codigo_funcionario = request.form['codigo_funcionario']
        codigo_ordem_servico = request.form['codigo_ordem_servico']
        item_ordem_servico = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        item_ordem_servico.execute('UPDATE item_ordem_servico SET codigo = %s, codigo_item_servico = %s, codigo_funcionario = %s, codigo_ordem_servico = %s WHERE id = %s', (codigo, codigo_item_servico, codigo_funcionario, codigo_ordem_servico, id))
        flash('Item Ordem Serviço atualizado com sucesso!')
        conn.commit()
        return redirect(url_for('app_item_ordem_servico.item_ordem_servico_all'))


@app_item_ordem_servico.route('/item-ordem-servico-delete/<id>', methods=['POST', 'GET'])
def item_ordem_servico_delete(id):
    item_ordem_servico = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    item_ordem_servico.execute('DELETE FROM item_ordem_servico WHERE id = {}'.format(id))
    conn.commit()
    flash('Item Ordem Serviço removido com sucesso!')
    return redirect(url_for('app_item_ordem_servico.item_ordem_servico_all'))