# atividades_api
Flask | Flask RESTFUL 
<br />
 ## :bookmark: Resume
API na qual é possível criar pessoas e atividades e atribuir atividades para as pessoas, salvando os dados no SQLITE via sqlalchemy
<br />

## Rodando o projeto
```
# Clone o projeto
git clone https://github.com/JhonataAugust0/atividades_api.git
# Navegue até o repositório
cd atividades_api
# Instale as dependências
pip install -r requirements.txt
# Rode o projeto 
python app.py
```
```
# Execute as requisições GET, POST, PUT e DELETE de acordo com as rotas definidas seguindo o padrão abaixo:
{
    "nome": "Desenvolver CRUD",
    "pessoa": "Adalberto"
}
# Para atividades
{
    "nome": "Adalberto",
    "idade": 23
}
# Para pessoas
```
