import sys
import requests

LOCAL='http://127.0.0.1:5000'
SERVER='https://orlok.pythonanywhere.com'
running=True

def post_request(nome,email,senha,endpoint):
  payload = {'nome':nome,'email': email, 'senha': senha}
  r = requests.post(endpoint+'/api/v1/admin', json=payload)
  print(r.text)
  
def create_admin():
  global running
  endpoint=''
  op=str(input('digite 1 para cadastrar localmente ou 2 para cadastrar no servidor: '))
  if op == '1':
    endpoint=LOCAL
  elif op == '2':
    endpoint=SERVER
  else:
    print('opção inválida.')
    #sys.exit()
    print()
    create_admin()
  nome=input(str('digite o nome do adm: '))
  email=input(str('digite o e-mail de acesso do administrador: '))
  senha=input(str('digite a senha de acesso do administrador: '))
  senha2=input(str('digite a senha novamente: '))
  if senha == senha2:
    post_request(nome,email,senha,endpoint)
    running=False
  else:
    print('as senhas não coincidem!')
  
def main():
  global running
  while running:
    cmd=str(input('digite 1 para criar um novo administrador: '))
    if cmd=='exit':
      running=False
      break
    elif cmd=='1':
      create_admin()

if __name__ == '__main__':
  main()