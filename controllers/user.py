from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from database import db
from database.models import User

user_bp=Blueprint('user_bp',__name__)

@user_bp.route('/',methods=['GET'])
@jwt_required()
def list_users():
  users = db.session.execute(db.select(User).order_by(User.id)).scalars()
  user_list=[user for user in users]
  return jsonify(user_list)
 
@user_bp.route('/',methods=['POST'])
def create_user():
  request_data=request.get_json()
  try:
    user=User(
    nome=request_data['nome'],
    email=request_data['email'],
    telefone=request_data['telefone'],
    senha=request_data['senha']
    )
    db.session.add(user)
    db.session.commit()
  except Exception as e:
    db.session.rollback()
    return jsonify({'error':str(e)})
  return jsonify({
    'response':'usúario cadastrado!'
  })
  
@user_bp.route('/<int:id>',methods=['GET'])
@jwt_required()
def get_user(id):
  try:
    user=db.get_or_404(User,id)
  except Exception as e:
    return jsonify({
      'response':'usúario não encontrado',
      'error':str(e)
    }),400
  return jsonify(user)
  
@user_bp.route('/<int:id>',methods=['PUT'])
@jwt_required()
def update_user(id):
  request_data=request.get_json()
  try:
    user=db.get_or_404(User,id)
    user.nome=request_data['nome']
    user.email=request_data['email']
    user.telefone=request_data['telefone']
    user.senha=request_data['senha']
    db.session.add(user)
    db.session.commit()
  except Exception as e:
    db.session.rollback()
    return jsonify({'error':str(e)})
  return jsonify({'response':'dados alterados'})
  
@user_bp.route('/<int:id>',methods=['DELETE'])
@jwt_required()
def delete_user(id):
  try:
    user=db.get_or_404(User,id)
    db.session.delete(user)
    db.session.commit()
  except Exception as e:
    return jsonify({'response':str(e)})
  return jsonify({'response':'usúario excluido'})