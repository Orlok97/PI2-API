import requests

def create_admin():
  email=input(str('digite o e-mail de acesso do administrador: '))
  senha=input(str('digite a senha de acesso do administrador: '))
  payload = {'email': email, 'senha': senha}
  r = requests.post('http://127.0.0.1:5000/api/v1/admin', json=payload)
  print(r.text)
  
def main():
  running=True
  print('digite: ')
  while running:
    cmd=str(input('>> '))
    if cmd=='exit':
      running=False
      break
    elif cmd=='token':
      t=generate_admin_access_token(cmd)
      print(t)

if __name__ == '__main__':
  main()
  #create_admin(EMAIL,SENHA)