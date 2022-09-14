from flask import Blueprint, render_template, request, redirect, url_for, flash
from dotenv import load_dotenv
import os
import psycopg2
import psycopg2.extras

load_dotenv()

app_nota_fiscal_servico = Blueprint('app_nota_fiscal_servico', __name__)
conn = psycopg2.connect(
            host= os.getenv("HOST"),
            database= os.getenv("DATABASE"),
            user= os.getenv("USER"),
            password= os.getenv("PASSWORD")
        )

@app_nota_fiscal_servico.route('/nota-fiscal-servico-all')
def nota_fiscal_servico_all():
    nota_fiscal_servico = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    nota_fiscal_servico.execute('SELECT * FROM nota_fiscal_servico')
    notas = nota_fiscal_servico.fetchall()
    return render_template('nota_fiscal_servico/ficha_nota_fiscal_servico.html', notas=notas)


@app_nota_fiscal_servico.route('/nota-fiscal-servico-add', methods=['POST'])
def nota_fiscal_servico_add():
    nota_fiscal_servico = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        codigo = request.form['codigo']
        cnpj_empresa = request.form['cnpj_empresa']
        cpf_cpnj_cliente = request.form['cpf_cnpj_cliente']
        codigo_ordem_servico = request.form['codigo_ordem_servico']
        total = request.form['total']
        forma_pagamento = request.form['forma_pagamento']
        nota_fiscal_servico.execute('INSERT INTO nota_fiscal_servico(codigo, cnpj_empresa, cpf_cnpj_cliente, codigo_ordem_servico, total, forma_pagamento) VALUES(%s, %s, %s, %s, %s, %s)', (codigo, cnpj_empresa, cpf_cpnj_cliente, codigo_ordem_servico, total, forma_pagamento))
        conn.commit()
        flash('Nota Fiscal Servico adicionado com sucesso!')
        return redirect(url_for('app_nota_fiscal_servico.nota_fiscal_servico_all'))


@app_nota_fiscal_servico.route('/nota-fiscal-servico-edit/<id>', methods=['POST', 'GET'])
def nota_fiscal_servico_edit(id):
    nota_fiscal_servico = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    nota_fiscal_servico.execute('SELECT * FROM nota_fiscal_servico WHERE id = {}'.format(id))
    data = nota_fiscal_servico.fetchall()
    nota_fiscal_servico.close()
    return render_template('nota_fiscal_servico/ficha_nota_fiscal_servico.html', nota_fis = data[0])


@app_nota_fiscal_servico.route('/nota-fiscal-servico-update/<id>', methods=['POST'])
def nota_fiscal_servico_update(id):
    if request.method == 'POST':
        codigo = request.form['codigo']
        cnpj_empresa = request.form['cnpj_empresa']
        cpf_cpnj_cliente = request.form['cpf_cnpj_cliente']
        codigo_ordem_servico = request.form['codigo_ordem_servico']
        total = request.form['total']
        forma_pagamento = request.form['forma_pagamento']
        nota_fiscal_servico = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        nota_fiscal_servico.execute('UPDATE nota_fiscal_servico SET codigo = %s, cnpj_empresa = %s, cpf_cnpj_cliente = %s, codigo_ordem_servico = %s, total = %s, forma_pagamento = %s WHERE id = %s', (codigo, cnpj_empresa, cpf_cpnj_cliente, codigo_ordem_servico, total, forma_pagamento, id))
        flash('Nota Fiscal Servico atualizado com sucesso!')
        conn.commit()
        return redirect(url_for('app_nota_fiscal_servico.nota_fiscal_servico_all'))


@app_nota_fiscal_servico.route('/nota-fiscal-servico-delete/<id>', methods=['POST', 'GET'])
def nota_fiscal_servico_delete(id):
    nota_fiscal_servico = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    nota_fiscal_servico.execute('DELETE FROM nota_fiscal_servico WHERE id = {}'.format(id))
    conn.commit()
    flash('Nota Fiscal Servico removido com sucesso!')
    return redirect(url_for('app_nota_fiscal_servico.nota_fiscal_servico_all'))