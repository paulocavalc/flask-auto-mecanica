from flask import Blueprint, render_template, request, redirect, url_for, flash
from dotenv import load_dotenv
import os
import psycopg2
import psycopg2.extras

load_dotenv()

app_cliente = Blueprint('app_cliente', __name__)

conn = psycopg2.connect(os.getenv("DATABASE_URL"))

@app_cliente.route('/cliente-all')
def cliente_all():
    cliente = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cliente.execute('SELECT * FROM cliente')
    clientes = cliente.fetchall()
    return render_template('cliente/ficha_cliente.html', clientes=clientes)


@app_cliente.route('/cliente-add', methods=['POST'])
def cliente_add():
    cliente = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        cpf_cnpj = request.form['cpf_cnpj']
        nome = request.form['nome']
        endereco = request.form['endereco']
        rg = request.form['rg']
        telefone = request.form['telefone']
        placa_carro = request.form['placa_carro']
        tipo = request.form['tipo']
        latitude = request.form['latitude']
        longitude = request.form['longitude']
        cliente.execute('INSERT INTO cliente(cpf_cnpj, nome, endereco, rg, telefone, placa_carro, tipo, latitude, longitude) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)', (cpf_cnpj, nome, endereco, rg, telefone, placa_carro, tipo, latitude, longitude))
        conn.commit()
        flash('Cliente adicionado com sucesso!')
        return redirect(url_for('app_cliente.cliente_all'))


@app_cliente.route('/cliente-edit/<id>', methods=['POST', 'GET'])
def cliente_edit(id):
    cliente = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cliente.execute('SELECT * FROM cliente WHERE id = {}'.format(id))
    data = cliente.fetchall()
    cliente.close()
    return render_template('cliente/ficha_cliente.html', client = data[0])


@app_cliente.route('/cliente-update/<id>', methods=['POST'])
def cliente_update(id):
    if request.method == 'POST':
        cpf_cnpj = request.form['cpf_cnpj']
        nome = request.form['nome']
        endereco = request.form['endereco']
        rg = request.form['rg']
        telefone = request.form['telefone']
        placa_carro = request.form['placa_carro']
        tipo = request.form['tipo']
        latitude = request.form['latitude']
        longitude = request.form['longitude']
        cliente = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cliente.execute('UPDATE cliente SET cpf_cnpj = %s, nome = %s, endereco = %s, rg = %s, telefone = %s, placa_carro = %s, tipo = %s, latitude = %s, longitude = %s WHERE id = %s', (cpf_cnpj, nome, endereco, rg, telefone, placa_carro, tipo, latitude, longitude, id))
        flash('Cliente atualizado com sucesso!')
        conn.commit()
        return redirect(url_for('app_cliente.cliente_all'))


@app_cliente.route('/cliente-delete/<id>', methods=['POST', 'GET'])
def cliente_delete(id):
    cliente = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cliente.execute('DELETE FROM cliente WHERE id = {}'.format(id))
    conn.commit()
    flash('Cliente removido com sucesso!')
    return redirect(url_for('app_cliente.cliente_all'))
