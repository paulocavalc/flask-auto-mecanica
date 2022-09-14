from flask import Blueprint, render_template, request, redirect, url_for, flash
from dotenv import load_dotenv
import os
import psycopg2
import psycopg2.extras

load_dotenv()

app_ordem_servico = Blueprint('app_ordem_servico', __name__)
conn = psycopg2.connect(
            host= os.getenv("HOST"),
            database= os.getenv("DATABASE"),
            user= os.getenv("USER"),
            password= os.getenv("PASSWORD")
        )

@app_ordem_servico.route('/ordem-servico-all')
def ordem_servico_all():
    ordem_servico = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    ordem_servico.execute('SELECT * FROM ordem_servico')
    ordens_servicos = ordem_servico.fetchall()
    return render_template('ordem_servico/ficha_ordem_servico.html', ordens_servicos=ordens_servicos)


@app_ordem_servico.route('/ordem-servico-add', methods=['POST'])
def ordem_servico_add():
    ordem_servico = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        codigo = request.form['codigo']
        entrada = request.form['entrada']
        saida = request.form['saida']
        codigo_funcionario = request.form['codigo_funcionario']
        placa_carro = request.form['placa_carro']
        cpf_cnpj_cliente = request.form['cpf_cnpj_cliente']
        ordem_servico.execute('INSERT INTO ordem_servico(codigo, entrada, saida, codigo_funcionario, placa_carro, cpf_cnpj_cliente) VALUES(%s, %s, %s, %s, %s, %s)', (codigo, entrada, saida, codigo_funcionario, placa_carro, cpf_cnpj_cliente))
        conn.commit()
        flash('Ordem Serviço adicionado com sucesso!')
        return redirect(url_for('app_ordem_servico.ordem_servico_all'))


@app_ordem_servico.route('/ordem-servico-edit/<id>', methods=['POST', 'GET'])
def ordem_servico_edit(id):
    ordem_servico = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    ordem_servico.execute('SELECT * FROM ordem_servico WHERE id = {}'.format(id))
    data = ordem_servico.fetchall()
    ordem_servico.close()
    return render_template('ordem_servico/ficha_ordem_servico.html', os = data[0])


@app_ordem_servico.route('/ordem-servico-update/<id>', methods=['POST'])
def ordem_servico_update(id):
    if request.method == 'POST':
        codigo = request.form['codigo']
        entrada = request.form['entrada']
        saida = request.form['saida']
        codigo_funcionario = request.form['codigo_funcionario']
        placa_carro = request.form['placa_carro']
        cpf_cnpj_cliente = request.form['cpf_cnpj_cliente']
        ordem_servico = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        ordem_servico.execute('UPDATE ordem_servico SET codigo = %s, entrada = %s, saida = %s, codigo_funcionario = %s, placa_carro = %s, cpf_cnpj_cliente = %s WHERE id = %s', (codigo, entrada, saida, codigo_funcionario, placa_carro, cpf_cnpj_cliente, id))
        flash('Ordem Serviço atualizado com sucesso!')
        conn.commit()
        return redirect(url_for('app_ordem_servico.ordem_servico_all'))


@app_ordem_servico.route('/ordem-servico-delete/<id>', methods=['POST', 'GET'])
def ordem_servico_delete(id):
    ordem_servico = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    ordem_servico.execute('DELETE FROM ordem_servico WHERE id = {}'.format(id))
    conn.commit()
    flash('Ordem Serviço removido com sucesso!')
    return redirect(url_for('app_ordem_servico.ordem_servico_all'))