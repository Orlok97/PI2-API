from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from database import db
from database.models import Admin

admin_bp=Blueprint('admin_bp',__name__)

@admin_bp.route('/',methods=['GET'])
def list_admin():
  admins = db.session.execute(db.select(Admin).order_by(Admin.id)).scalars()
  admin_list=[adm for adm in admins]
  return jsonify(admin_list)

@admin_bp.route('/',methods=['POST'])
def create_admin():
  request_data=request.get_json()
  admin=Admin(
  email=request_data['email'],
  senha=request_data['senha']
  )
  db.session.add(admin)
  db.session.commit()
  return jsonify({'response':'admin criado com sucesso.'})

@admin_bp.route('/<int:id>',methods=['PUT'])
def update_admin(id):
  pass