from flask import Blueprint, render_template, request, redirect, url_for, flash
from dotenv import load_dotenv
import os
import psycopg2
import psycopg2.extras

load_dotenv()

app_item_servico = Blueprint('app_item_servico', __name__)
conn = psycopg2.connect(
            host= os.getenv("HOST"),
            database= os.getenv("DATABASE"),
            user= os.getenv("USER"),
            password= os.getenv("PASSWORD")
        )

@app_item_servico.route('/item-servico-all')
def item_servico_all():
    item_servico = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    item_servico.execute('SELECT * FROM item_servico')
    itens_servicos = item_servico.fetchall()
    return render_template('item_servico/ficha_item_servico.html', itens_servicos=itens_servicos)


@app_item_servico.route('/item-servico-add', methods=['POST'])
def item_servico_add():
    item_servico = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        codigo = request.form['codigo']
        descricao = request.form['descricao']
        valor_item = request.form['valor_item']
        codigo_servico = request.form['codigo_servico']
        item_servico.execute('INSERT INTO item_servico(codigo, descricao, valor_item, codigo_servico) VALUES(%s, %s, %s, %s)', (codigo, descricao, valor_item, codigo_servico))
        conn.commit()
        flash('Item Serviço adicionado com sucesso!')
        return redirect(url_for('app_item_servico.item_servico_all'))


@app_item_servico.route('/item-servico-edit/<id>', methods=['POST', 'GET'])
def item_servico_edit(id):
    item_servico = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    item_servico.execute('SELECT * FROM item_servico WHERE id = {}'.format(id))
    data = item_servico.fetchall()
    item_servico.close()
    return render_template('item_servico/ficha_item_servico.html', itens = data[0])


@app_item_servico.route('/item-servico-update/<id>', methods=['POST'])
def item_servico_update(id):
    if request.method == 'POST':
        codigo = request.form['codigo']
        descricao = request.form['descricao']
        valor_item = request.form['valor_item']
        codigo_servico = request.form['codigo_servico']
        item_servico = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        item_servico.execute('UPDATE item_servico SET codigo = %s, descricao = %s, valor_item = %s, codigo_servico = %s WHERE id = %s', (codigo, descricao, valor_item, codigo_servico, id))
        flash('Item Serviço atualizado com sucesso!')
        conn.commit()
        return redirect(url_for('app_item_servico.item_servico_all'))


@app_item_servico.route('/item-servico-delete/<id>', methods=['POST', 'GET'])
def item_servico_delete(id):
    item_servico = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    item_servico.execute('DELETE FROM item_servico WHERE id = {}'.format(id))
    conn.commit()
    flash('Item Serviço removido com sucesso!')
    return redirect(url_for('app_item_servico.item_servico_all'))
