from flask import Flask, request
from flask_restful import Resource, Api
from models import Pessoa, Atividades

app = Flask(__name__)
api = Api(app)


class Pessoas(Resource):
  def get(self, nome):
    pessoa = Pessoa.query.filter_by(nome=nome).first()
    try:
      response = {
        'nome': pessoa.nome,
        'idade': pessoa.idade,
        'id': pessoa.id
      }
    except AttributeError:
      response = {'status': 'Error', 'message': 'Pessoa não encontrada'}
    return response

  def put(self, nome):
    pessoa = Pessoa.query.filter_by(nome=nome).first()
    data = request.json
    if 'nome' in data:
      pessoa.nome = data['nome']
    if 'idade' in data:
      pessoa.idade = data['idade']
    pessoa.save_pessoa()
    response = {
      'id': pessoa.id,
      'nome': pessoa.nome,
      'idade': pessoa.idade 
    }
    return response

  def delete(self, nome):
    pessoa = Pessoa.query.filter_by(nome=nome).first()
    pessoa.delete_pessoa()
    message = (f'Pessoa {pessoa.nome} excluída')
    return {'status': 'success', 'message': message}


class Pessoa_list(Resource):
  def get(self):
    pessoas = Pessoa.query.all()
    response = [{'id': p.id, 'nome': p.nome, 'idade': p.idade}  for p in pessoas ]
    return response
  def post(self):
    data = request.json
    pessoa = Pessoa(nome=data['nome'], idade=data['idade'])
    pessoa.save_pessoa()
    response = {
      'id': pessoa.id,
      'idade': pessoa.id,
      'nome': pessoa.nome
    }
    return response


class Atividades_list(Resource):
  def get(self):
    atividades = Atividades.query.all()
    response = [{'id': a.id, 'nome': a.nome, 'pessoa': a.pessoa.nome} for a in atividades]
    return response  

  def post(self):
    data = request.json
    pessoa = Pessoa.query.filter_by(nome=data['pessoa']).first()
    atividade = Atividades(nome=data['nome'], pessoa=pessoa)
    atividade.save_atividades()
    response = {
      'pessoa': atividade.pessoa.nome,
      'nome': atividade.nome,
      'id': atividade.id
    }
    return response

api.add_resource(Pessoas, '/pessoas/<string:nome>/')
api.add_resource(Pessoa_list, '/pessoas/')
api.add_resource(Atividades_list, '/atividades/')

if __name__ == '__main__':
  app.run(debug=True)