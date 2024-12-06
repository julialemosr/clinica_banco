from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, declarative_base

engine = create_engine('sqlite:///base_vet_analise.sqlite3')

db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Veterinario(Base):
    __tablename__ = 'TAB_VETERINARIO'
    id_vet2 = Column(Integer, primary_key=True)
    salario2 = Column(Float, nullable=False, index=True)
    nomeVet = Column(String(40), nullable=False)
    crmv = Column(Integer, nullable=False, index=True, unique=True)
    v_consulta2 = Column(Float, nullable=False, index=True)


    def __repr__(self):
        return '<Veterinario: {} {} {} >'.format(self.id_vet2, self.nomeVet, self.crmv)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize_veterinario(self):
        dados_vet = {
            "id_vet": self.id_vet2,
            "salario_vet": self.salario2,
            "nome_vet": self.nomeVet,
            "crmv_vet": self.crmv,
            "consulta_vet": self.v_consulta2,
        }
        return dados_vet


class Motivo(Base):
    __tablename__ = 'TAB_MOTIVO'
    id_motivo = Column(Integer, primary_key=True)
    nome_motivo = Column(String(70), nullable=False, index=True)
    motivo_categoria = Column(String(50), nullable=False, index=True)
    valor_motivo = Column(Float, nullable=False, index=True)

    def __repr__(self):
        return '<Motivo: {} {} {} >'.format(self.id_motivo, self.nome_motivo, self.motivo_categoria)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize_motivo(self):
        dados_motivo = {
            "id_motivo": self.id_motivo,
            "nome_motivo": self.nome_motivo,
            "motivo_categoria": self.motivo_categoria,
            "valor_motivo": self.valor_motivo,
        }
        return dados_motivo


class Consulta(Base):
    __tablename__ = 'TAB_CONSULTA'
    idConsulta = Column(Integer, primary_key=True)
    motivo_id2 = Column(Integer,ForeignKey('TAB_MOTIVO.id_motivo'))
    motivo = relationship('Motivo')
    hora2 = Column(Integer, nullable=False, index=True)
    minuto = Column(Integer, nullable=False, index=True)
    data2 = Column(String(8), nullable=False, index=True)
    idAnimal2 = Column(Integer, ForeignKey('TAB_ANIMAL.id_animal'))
    animal = relationship('Animal')
    idVeterinario2 = Column(Integer, ForeignKey('TAB_VETERINARIO.id_vet2'))
    veterinario = relationship('Veterinario')

    def __repr__(self):
        return '<Consulta: {} {} {} {} {} {} >'.format(self.idConsulta, self.minuto, self.hora2,
                                                 self.data2, self.idVeterinario2, self.motivo_id2)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize_consulta(self):
        dados_consulta = {
            "idConsulta": self.idConsulta,
            "motivo_id2": self.motivo_id2,
            "hora2": self.hora2,
            "minuto": self.minuto,
            "data2": self.data2,
            "idAnimal2": self.idAnimal2,
            "idVeterinario2": self.idVeterinario2,
        }
        return dados_consulta


class Cliente(Base):
    __tablename__ = 'TAB_CLIENTE'
    id_cliente = Column(Integer, primary_key=True, autoincrement=True)
    CPF = Column(String(11), nullable=False, index=True, unique=True)
    Nome2 = Column(String(40), nullable=False, index=True)
    telefone = Column(String(20), nullable=False, index=True)
    Profissa2 = Column(String(70), index=True)
    Area2 = Column(String(30), index=True)


    def __repr__(self):
        return '<Cliente: {} {} {} {} {} {} >'.format(self.id_cliente, self.CPF, self.Nome2, self.telefone, self.Area2, self.Profissa2)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize_cliente(self):
        dados_cliente = {
            "id_cliente": self.id_cliente,
            "CPF": self.CPF,
            "Nome2": self.Nome2,
            "telefone": self.telefone,
            "Profissao": self.Profissa2,
            "Area2": self.Area2,
        }
        return dados_cliente


class Animal(Base):
    __tablename__ = 'TAB_ANIMAL'
    id_animal = Column(Integer, primary_key=True)
    nome_animal = Column(String(30), nullable=False, index=True)
    raca2 = Column(String(30), nullable=False, index=True)
    anoNasci2 = Column(Integer, nullable=False, index=True)
    idCliente2 = Column(Integer, ForeignKey('TAB_CLIENTE.id_cliente'))
    cliente = relationship('Cliente')

    def __repr__(self):
        return '<Cliente: {} {} {} {} >'.format(self.id_animal, self.nome_animal, self.raca2, self.idCliente2)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize_animal(self):
        dados_animal = {
            "id_animal": self.id_animal,
            "nome_animal": self.nome_animal,
            "raca2": self.raca2,
            "anoNasci2": self.anoNasci2,
            "idCliente2": self.idCliente2,
        }
        return dados_animal


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_db()
