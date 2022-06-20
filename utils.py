from django import db
from models import Pessoa

# Métodos auxiliares da tabelas Pessoa
def insert_pessoa():
  pessoa = Pessoa(nome='Adalberto', idade=35)
  pessoa.save_pessoa()
  return print(f'insert {pessoa}')


def consult_pessoa():
  pessoa = Pessoa.query.all()
  print(f'consult {pessoa}')
  pessoa = Pessoa.query.filter_by(nome='Adalberto').first()
  print(f'consult filter {pessoa}')

def change_pessoa():
  pessoa = Pessoa.query.filter_by(nome='Adalberto').first()
  pessoa.idade = 21
  pessoa.save_pessoa()
  return print('pessoa alterada')

def delete_pessoa():
  pessoa = Pessoa.query.filter_by(nome='Adalberto').first()
  pessoa.delete_pessoa()

  
if __name__ == '__main__':
  # insert_pessoa()
  consult_pessoa()
  change_pessoa()
  delete_pessoa()