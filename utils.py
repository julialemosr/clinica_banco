from models import Veterinario, Motivo, Consulta, Cliente, Animal, db_session
from sqlalchemy import select


#inserir dados na tabela
def inserir_veterinario():
    veterinario = Veterinario(nomeVet=str(input('Nome do veterinário: ')),
                              salario2=float(input('Salário: ')),
                              crmv=int(input('crmv: ')),
                              v_consulta2=float(input('Valor da consulta: ')),
                              )
    print(veterinario)
    veterinario.save()


def consultar_veterinario():
    var_veterinario = select(Veterinario)
    var_veterinario = db_session.execute(var_veterinario).all()
    print(var_veterinario)


def atualizar_veterinario():
    var_veterinario = select(Veterinario).where(Veterinario.nomeVet == str(input('Nome: ')) == Veterinario.nomeVet)
    var_veterinario = select(Veterinario).where(Veterinario.salario2 == float(input('Salário: ')) == Veterinario.salario2)
    var_veterinario = select(Veterinario).where(Veterinario.crmv == int(input('crmv: ')) == Veterinario.crmv)
    var_veterinario = db_session.execute(var_veterinario).scalar()
    print(var_veterinario)
    var_veterinario.nomeVet = str(input('Novo nome: '))
    var_veterinario.salario2 = (float('Novo salário: '))
    var_veterinario.crmv = int(input('Novo crmv: '))
    var_veterinario.save()

def deletar_veterinario():
    veterinario_deletar = input('Qual veterinário você deseja deletar? ')
    var_veterinario = select(Veterinario).where(veterinario_deletar == Veterinario.nomeVet)
    var_veterinario = db_session.execute(var_veterinario).scalar()
    var_veterinario.delete()


def inserir_motivo():
    motivo = Motivo(nome_motivo=str(input('Nome do motivo: ')),
                              valor_motivo=float(input('Valor do motivo: ')),
                              motivo_categoria=str(input('Categoria do motivo: '))
                              )
    print(motivo)
    motivo.save()


def consultar_motivo():
    var_motivo = select(Motivo)
    var_motivo = db_session.execute(var_motivo).all()
    print(var_motivo)


def atualizar_motivo():
    var_motivo = select(Motivo).where(Motivo.nome_motivo == str(input('Nome do motivo: ')) == Motivo.nome_motivo)
    var_motivo = select(Motivo).where(Motivo.valor_motivo == (float('Valor do motivo: ')) == Motivo.valor_motivo)
    var_motivo = select(Motivo).where(Motivo.motivo_categoria == str(input('Categoria do motivo: ')) == Motivo.motivo_categoria)
    var_motivo = db_session.execute(var_motivo).scalar()
    print(var_motivo)
    var_motivo.nome_motivo = str(input('Novo nome para a categoria: '))
    var_motivo.valor_motivo = (float('Novo valor do motivo: '))
    var_motivo.motivo_categoria = str(input('Nova categoria do motivo: '))
    var_motivo.save()

def deletar_motivo():
    motivo_deletar = input('Qual motivo você deseja deletar? ')
    var_motivo = select(Motivo).where(motivo_deletar == Motivo.nome_motivo)
    var_motivo = db_session.execute(var_motivo).scalar()
    var_motivo.delete()



def inserir_consulta():
    consulta = Consulta(data2=str(input('Data da consulta: ')),
                    hora2=int(input('Hora da consulta: ')),
                    minuto=int(input('minutos da consulta: '))
                    )
    print(consulta)
    consulta.save()


def consultar_consulta():
    var_consulta = select(Consulta)
    var_consulta = db_session.execute(var_consulta).all()
    print(var_consulta)


def atualizar_consulta():
    var_consulta = select(Consulta).where(Consulta.data2 == str(input('Data da consulta: ')) == Consulta.data2)
    var_consulta = select(Consulta).where(Consulta.hora2 == int(input('Valor da consulta: ')) == Consulta.hora2)
    var_consulta = db_session.execute(var_consulta).scalar()
    print(var_consulta)
    var_consulta.data2 = str(input('Nova data da consulta: '))
    var_consulta.hora2 = int(input('Novo valor da consulta: '))
    var_consulta.save()


def deletar_consulta():
    consulta_deletar = input('Qual data você deseja deletar? ')
    consulta_deletar = input('Qual hora você deseja deletar? ')
    var_consulta = select(Consulta).where(consulta_deletar == Consulta.data2)
    var_consulta = select(Consulta).where(consulta_deletar == Consulta.hora2)
    var_consulta = db_session.execute(var_consulta).scalar()
    var_consulta.delete()


def inserir_cliente():
    cliente = Cliente(Nome2=str(input('Nome do cliente: ')),
                    CPF=str(input('CPF do cliente: ')),
                    telefone=str(input('Telefone do cliente: '))
                    )
    print(cliente)
    cliente.save()


def consultar_cliente():
    var_cliente = select(Cliente)
    var_cliente = db_session.execute(var_cliente).all()
    print(var_cliente)


def atualizar_cliente():
    var_cliente = select(Cliente).where(Cliente.Nome2 == str(input('Nome do cliente: ')) == Cliente.Nome2)
    var_cliente = select(Cliente).where(Cliente.CPF == str(input('CPF do cliente: ')) == Cliente.CPF)
    var_cliente = select(Cliente).where(Cliente.telefone == str(input('Telefone do cliente: ')) == Cliente.telefone)
    var_cliente = db_session.execute(var_cliente).scalar()
    print(var_cliente)
    var_cliente.Nome2 = str(input('Novo nome do cliente: '))
    var_cliente.CPF = str(input('Novo CPF do cliente: '))
    var_cliente.telefone = str(input('Novo telefone do cliente: '))
    var_cliente.save()


def deletar_cliente():
    cliente_deletar = input('Qual cliente você deseja deletar? ')
    var_cliente = select(Cliente).where(cliente_deletar == Cliente.Nome2)
    var_cliente = db_session.execute(var_cliente).scalar()
    var_cliente.delete()





def inserir_animal():
    animal = Animal(nome_animal=str(input('Nome do animal: ')),
                    raca2=str(input('raça do animal: ')),
                    anoNasci2=int(input('Ano de nascimento do animal: '))
                    )
    print(animal)
    animal.save()


def consultar_animal():
    var_animal = select(Animal)
    var_animal = db_session.execute(var_animal).all()
    print(var_animal)


def atualizar_animal():
    var_animal = select(Animal).where(Animal.nome_animal == str(input('Nome do animal: ')) == Animal.nome_animal)
    var_animal = select(Animal).where(Animal.raca2 == str(input('raça do animal: ')) == Animal.raca2)
    var_animal = select(Animal).where(Animal.anoNasci2 == int(input('Ano de nascimento do animal: ')) == Animal.anoNasci2)
    var_animal = db_session.execute(var_animal).scalar()
    print(var_animal)
    var_animal.nome_animal = str(input('Novo nome do animal: '))
    var_animal.raca2 = str(input('Nova raça do animal: '))
    var_animal.anoNasci2 = int(input('Novo ano de nascimento do animal: '))
    var_animal.save()


def deletar_animal():
    animal_deletar = input('Qual animal você deseja deletar? ')
    var_animal = select(Animal).where(animal_deletar == Animal.nome_animal)
    var_animal = db_session.execute(var_animal).scalar()
    var_animal.delete()

if __name__ == '__main__':

    while True:
        print("MENU")
        print('1 - inserir veterinário')
        print("2 - consultar veterinário")
        print("3 - inserir motivo")
        print("4 - consultar motivo")
        print("5 - inserir consulta")
        print("6 - consultar consulta")
        print("7 - inserir cliente")
        print("8 - consultar cliente")
        print("9 - inserir animal")
        print("10 - consultar animal")
        print("0 - sair")


        escolha = input("Escolha uma das opções: ")
        if escolha == '1':
            inserir_veterinario()
        elif escolha == '2':
            consultar_veterinario()
        elif escolha == '3':
            inserir_motivo()
        elif escolha == '4':
            consultar_motivo()
        elif escolha == '5':
            inserir_consulta()
        elif escolha == '6':
            consultar_consulta()
        elif escolha == '7':
            inserir_cliente()
        elif escolha == '8':
            consultar_cliente()
        elif escolha == '9':
            inserir_animal()
        elif escolha == '10':
            consultar_animal()
        elif escolha == '0':
            break