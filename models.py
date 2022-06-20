from pip import main
from sqlalchemy import ForeignKey, create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///activities.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Pessoa(Base):
  """Criação da arquitetura da tabela com seus dados e méto-
  dos."""
  __tablename__ = 'Pessoa'
  id = Column(Integer, primary_key=True)
  nome = Column(String(40), index=True)
  idade = Column(Integer)

  def __repr__(self):
    return (f'<Pessoa {self.nome}>')

  def save_pessoa(self):
    db_session.add(self)
    db_session.commit()
    return print('Committed successfully')

  def delete_pessoa(self):
    db_session.delete(self)
    db_session.commit()
    return print('Deleted successfully')

class Atividades(Base):
  """Criação da tabela de atividades contendo seus dados ne-
  cessários."""
  __tablename__ = 'Atividades'
  id = Column(Integer, primary_key=True)
  nome = Column(String(80))
  pessoa_id = Column(Integer, ForeignKey('Pessoa.id'))
  pessoa = relationship('Pessoa')

  def __repr__(self):
    return (f'<Atividades {self.nome}>')


  def save_atividades(self):
    db_session.add(self)
    db_session.commit()
    return print('Committed successfully')

  def delete_atividades(self):
    db_session.delete(self)
    db_session.commit()
    return print('Deleted successfully')


def init_db():
  Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
  init_db()