from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from database import db
from database.models import Admin, Employee

admin_bp=Blueprint('admin_bp',__name__)

def create_admin_employee(nome, email, senha):
  admin_employee=Employee(
   nome=nome,
   email=email,
   senha=senha,
   cargo='admin'
    )
  db.session.add(admin_employee)
  db.session.commit()
  print('admin employee criado')
  
@admin_bp.route('/',methods=['GET'])
def list_admin():
  admins = db.session.execute(db.select(Admin).order_by(Admin.id)).scalars()
  admin_list=[adm for adm in admins]
  return jsonify(admin_list)

@admin_bp.route('/',methods=['POST'])
def create_admin():
  request_data=request.get_json()
  admin=Admin(
  nome=request_data['nome'],
  email=request_data['email'],
  senha=request_data['senha']
  )
  db.session.add(admin)
  db.session.commit()
  create_admin_employee(request_data['nome'],request_data['email'],request_data['senha'])
  return jsonify({'response':'admin criado com sucesso.'})

@admin_bp.route('/<int:id>',methods=['PUT'])
def update_admin(id):
  pass