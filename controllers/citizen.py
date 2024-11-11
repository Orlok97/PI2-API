from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from database import db
from database.models import Citizen, Janitorial
from controllers.auth import auth_citizen
from modules.upload import upload

citizen_bp=Blueprint('citizen_bp',__name__)

@citizen_bp.route('/',methods=['GET'])
@jwt_required()
def list_citizens():
  citizens = db.session.execute(db.select(Citizen).order_by(Citizen.id)).scalars()
  citizen_list=[citizen for citizen in citizens]
  return jsonify(citizen_list)
 
@citizen_bp.route('/',methods=['POST'])
def create_citizen():
  request_data=request.get_json()
  try:
    citizen=Citizen(
    nome=request_data['nome'],
    email=request_data['email'],
    telefone=request_data['telefone'],
    senha=request_data['senha']
    )
    db.session.add(citizen)
    db.session.commit()
  except Exception as e:
    db.session.rollback()
    return jsonify({'error':str(e)})
  return jsonify({
    'response':'usúario cadastrado!'
  })
  
@citizen_bp.route('/<int:id>',methods=['GET'])
@jwt_required()
def get_citizen(id):
  try:
    citizen=db.get_or_404(Citizen,id)
  except Exception as e:
    return jsonify({
      'response':'usúario não encontrado',
      'error':str(e)
    }),400
  return jsonify(citizen)
  
@citizen_bp.route('/<int:id>',methods=['PUT'])
@jwt_required()
def update_citizen(id):
  request_data=request.form.to_dict()
  try:
    file = request.files['file']
    filename=upload(file,'profile/')
  except Exception as e:
    print('erro ',e)
    filename=None
  print(filename)
  try:
    citizen=db.get_or_404(Citizen,id)
    #citizen.nome=request_data['nome']
    citizen.telefone=request_data['telefone']
    citizen.senha=request_data['senha']
    citizen.foto=filename
    db.session.add(citizen)
    db.session.commit()
  except Exception as e:
    db.session.rollback()
    return jsonify({'error':str(e)})
  return jsonify({'response':'dados alterados'})
  
@citizen_bp.route('/<int:id>',methods=['DELETE'])
@jwt_required()
def delete_citizen(id):
  try:
    citizen=db.get_or_404(Citizen,id)
    db.session.delete(citizen)
    db.session.commit()
  except Exception as e:
    return jsonify({'response':str(e)})
  return jsonify({'response':'usúario excluido'})

@citizen_bp.route('/requests',methods=['GET'])
@jwt_required()
def list_citizen_requests():
  citizen=auth_citizen()
  citizen_requests=Janitorial.query.filter_by(user_id=citizen.id).all()
  return jsonify(citizen_requests)