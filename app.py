from flask import Flask, render_template, request, redirect, flash, url_for
from controller.carro_controller import app_carro
from controller.cliente_controller import app_cliente
from controller.empresa_controller import app_empresa
from controller.funcionario_controller import app_funcionario
from controller.item_ordem_servico_controller import app_item_ordem_servico
from controller.item_servico_controller import app_item_servico
from controller.nota_fiscal_servico_controller import app_nota_fiscal_servico
from controller.ordem_servico_controller import app_ordem_servico
from controller.servico_controller import app_servico
from dotenv import load_dotenv
import os

load_dotenv()


app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")


app.register_blueprint(app_carro)
app.register_blueprint(app_cliente)
app.register_blueprint(app_empresa)
app.register_blueprint(app_funcionario)
app.register_blueprint(app_item_ordem_servico)
app.register_blueprint(app_item_servico)
app.register_blueprint(app_nota_fiscal_servico)
app.register_blueprint(app_ordem_servico)
app.register_blueprint(app_servico)


@app.route('/')
def home():
    return render_template('login/login.html')


@app.route('/login-sucesso', methods=['POST'])
def autenticar():
    usuario = request.form.get('usuario')
    password = request.form.get('password')
    if (usuario == '85540079911') and (password == 'admin2022'):
        flash('Login efetuado com sucesso!')
        return redirect(url_for('auto_mecanica'))
    else:
        flash('Login inválido!')
    return redirect('/')


@app.route('/auto-mecanica')
def auto_mecanica():
    return render_template('layout/base.html')


@app.route('/emitir-fatura')
def emitir():
    return render_template('emitir_fatura/emitir_fatura.html')


if __name__ == '__main__':
    app.run(debug=True)