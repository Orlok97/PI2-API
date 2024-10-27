import requests

def create_admin():
  nome=input(str('digite o nome do adm: '))
  email=input(str('digite o e-mail de acesso do administrador: '))
  senha=input(str('digite a senha de acesso do administrador: '))
  payload = {'nome':nome,'email': email, 'senha': senha}
  r = requests.post('https://orlok.pythonanywhere.com/api/v1/admin', json=payload)
  print(r.text)
  
def main():
  running=True
  print('digite: 1 para cadastrar o administrador')
  while running:
    cmd=str(input('>> '))
    if cmd=='exit':
      running=False
      break
    elif cmd=='1':
      create_admin()

if __name__ == '__main__':
  main()