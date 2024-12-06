from flask import Flask, render_template, request, redirect, url_for, flash
from sqlalchemy import select
from models import Veterinario, Motivo, Consulta, Cliente, Animal, db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'


@app.route('/')
def inicio():
    return render_template('base.html')


@app.route('/veterinarios', methods=['GET', 'POST'])
def veterinarios():
    sql_veterinarios = select(Veterinario)
    resultado_veterinarios = db_session.execute(sql_veterinarios).scalars()
    lista_veterinarios = []
    for n in resultado_veterinarios:
        lista_veterinarios.append(n.serialize_veterinario())
        print(lista_veterinarios[-1])
    return render_template("lista_veterinarios.html",
                           lista_veterinarios=lista_veterinarios)


@app.route('/motivos', methods=['GET', 'POST'])
def motivos():
    sql_motivos = select(Motivo)
    resultado_motivos = db_session.execute(sql_motivos).scalars()
    lista_motivos = []
    for n in resultado_motivos:
        lista_motivos.append(n.serialize_motivo())
        print(lista_motivos[-1])
    return render_template("lista_motivos.html",
                           lista_motivos=lista_motivos)


@app.route('/consultas', methods=['GET', 'POST'])
def consultas():
    sql_consultas = select(Consulta)
    resultado_consultas = db_session.execute(sql_consultas).scalars()
    lista_consultas = []
    for n in resultado_consultas:
        lista_consultas.append(n.serialize_consulta())
        print(lista_consultas[-1])
    return render_template("lista_consultas.html",
                           lista_consultas=lista_consultas)


@app.route('/clientes', methods=['GET', 'POST'])
def clientes():
    sql_clientes = select(Cliente)
    resultado_clientes = db_session.execute(sql_clientes).scalars()
    lista_clientes = []
    for n in resultado_clientes:
        lista_clientes.append(n.serialize_cliente())
        print(lista_clientes[-1])
    return render_template("lista_clientes.html",
                           lista_clientes=lista_clientes)


@app.route('/animais', methods=['GET', 'POST'])
def animais():
    sql_animais = select(Animal)
    resultado_animais = db_session.execute(sql_animais).scalars()
    lista_animais = []
    for n in resultado_animais:
        lista_animais.append(n.serialize_animal())
        print(lista_animais[-1])
    return render_template("lista_animais.html",
                           lista_animais=lista_animais)


@app.route('/novo_veterinarios', methods=['POST', 'GET'])
def criar_veterinario():
    if request.method == "POST":
        if not request.form['form-nomeVet']:
            flash("Preencher todos os campos!! ", "error")
        if not request.form['form-salario2']:
            flash("Preencher todos os campos!! ", "error")
        if not request.form['form-crmv']:
            flash("Preencher todos os campos!! ", "error")

        else:
            form_evento = Veterinario(nomeVet=str(request.form['form-nomeVet']),
                                      salario2=float(request.form['form-salario2']),
                                      crmv=int(request.form['form-crmv']),
                                      v_consulta2=float(request.form['form-v_consulta2']),
                                      )
            print(form_evento)
            form_evento.save()
            db_session.close()
            flash("VETERINÁRIO ADICIONADA COM SUCESSO!!", "success")
            return redirect(url_for('veterinarios'))

    return render_template('novo_veterinarios.html')


@app.route('/novo_motivos', methods=['POST', 'GET'])
def criar_motivo():
    if request.method == "POST":
        if not request.form['form-nome_motivo']:
            flash("Preencher todos os campos!! ", "error")
        if not request.form['form-valor_motivo']:
            flash("Preencher todos os campos!! ", "error")
        if not request.form['form-motivo_categoria']:
            flash("Preencher todos os campos!! ", "error")

        else:
            form_evento = Motivo(nome_motivo=str(request.form['form-nome_motivo']),
                                 valor_motivo=float(request.form['form-valor_motivo']),
                                 motivo_categoria=str(request.form['form-motivo_categoria'])
                                 )
            print(form_evento)
            form_evento.save()
            db_session.close()
            flash("PESSOA ADICIONADA COM SUCESSO!!", "success")
            return redirect(url_for('motivos'))

    return render_template('novo_motivo.html')


@app.route('/nova_consultas', methods=['POST', 'GET'])
def criar_consulta():
    if request.method == "POST":
        if not request.form['form-data2']:
            flash("Preencher todos os campos!! ", "error")
        if not request.form['form-hora2']:
            flash("Preencher todos os campos!! ", "error")

        else:
            form_evento = Consulta(data2=str(request.form['form-data2']),
                                   hora2=int(request.form['form-hora2']),
                                   minuto=int(request.form['form-hora2'])
                                   )
            print(form_evento)
            form_evento.save()
            db_session.close()
            flash("PESSOA ADICIONADA COM SUCESSO!!", "success")
            return redirect(url_for('consultas'))

    return render_template('nova_consulta.html')


@app.route('/novo_clientes', methods=['POST', 'GET'])
def criar_clientes():
    if request.method == "POST":
        if not request.form['form-Nome2']:
            flash("Preencher todos os campos!! ", "error")
        if not request.form['form-CPF']:
            flash("Preencher todos os campos!! ", "error")
        if not request.form['form-telefone']:
            flash("Preencher todos os campos!! ", "error")

        else:
            form_evento = Cliente(Nome2=str(request.form['form-Nome2']),
                                  CPF=str(request.form['form-CPF']),
                                  telefone=str(request.form['form-telefone'])
                                  )
            print(form_evento)
            form_evento.save()
            db_session.close()
            flash("PESSOA ADICIONADA COM SUCESSO!!", "success")
            return redirect(url_for('clientes'))

    return render_template('novo_cliente.html')


@app.route('/novo_animais', methods=['POST', 'GET'])
def criar_animal():
    if request.method == "POST":
        if not request.form['form-nome_animal']:
            flash("Preencher todos os campos!! ", "error")
        if not request.form['form-raca2']:
            flash("Preencher todos os campos!! ", "error")
        if not request.form['form-anoNasci2']:
            flash("Preencher todos os campos!! ", "error")

        else:
            form_evento = Animal(nome_animal=str(request.form['form-nome_animal']),
                                 raca2=str(request.form['form-raca2']),
                                 anoNasci2=int(request.form['form-anoNasci2'])
                                 )
            print(form_evento)
            form_evento.save()
            db_session.close()
            flash("PESSOA ADICIONADA COM SUCESSO!!", "success")
            return redirect(url_for('animais'))

    return render_template('novo_animal.html')


if __name__ == '__main__':
    app.run(debug=True)
