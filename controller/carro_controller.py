from flask import Blueprint, render_template, request, redirect, url_for, flash
from dotenv import load_dotenv
import os
import psycopg2
import psycopg2.extras

load_dotenv()

app_carro = Blueprint('app_carro', __name__)

conn = psycopg2.connect(os.getenv("DATABASE_URL"))

#conn = psycopg2.connect(
#            host= os.getenv("HOST"),
#            database= os.getenv("DATABASE"),
#            user= os.getenv("USER"),
#            password= os.getenv("PASSWORD")
#        )

@app_carro.route('/carro-all')
def carro_all():
    carro = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    carro.execute('SELECT * FROM carro')
    carros = carro.fetchall()
    return render_template('carro/ficha_carro.html', carros=carros)


@app_carro.route('/carro-add', methods=['POST'])
def carro_add():
    carro = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        placa_carro = request.form['placa_carro']
        modelo = request.form['modelo']
        marca = request.form['marca']
        carro.execute('INSERT INTO carro(placa_carro, modelo, marca) VALUES(%s, %s, %s)', (placa_carro, modelo, marca))
        conn.commit()
        flash('Carro adicionado com sucesso!')
        return redirect(url_for('app_carro.carro_all'))


@app_carro.route('/carro-edit/<id>', methods=['POST', 'GET'])
def carro_edit(id):
    carro = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    carro.execute('SELECT * FROM carro WHERE id = {}'.format(id))
    data = carro.fetchall()
    carro.close()
    return render_template('carro/ficha_carro.html', car = data[0])


@app_carro.route('/carro-update/<id>', methods=['POST'])
def carro_update(id):
    if request.method == 'POST':
        placa_carro = request.form['placa_carro']
        modelo = request.form['modelo']
        marca = request.form['marca']
        carro = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        carro.execute('UPDATE carro SET placa_carro = %s, modelo = %s, marca = %s WHERE id = %s', (placa_carro, modelo, marca, id))
        flash('Carro atualizado com sucesso!')
        conn.commit()
        return redirect(url_for('app_carro.carro_all'))


@app_carro.route('/carro-delete/<id>', methods=['POST', 'GET'])
def carro_delete(id):
    carro = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    carro.execute('DELETE FROM carro WHERE id = {}'.format(id))
    conn.commit()
    flash('Carro removido com sucesso!')
    return redirect(url_for('app_carro.carro_all'))
