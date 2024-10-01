from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from database import db
from database.models import Janitorial
from controllers.auth import auth_user
from datetime import datetime

janitorial_bp=Blueprint('janitorial_bp',__name__)

@janitorial_bp.route('/',methods=['GET'])
@jwt_required()
def get_requests():
  reqs=db.session.execute(db.select(Janitorial).order_by(Janitorial.id)).scalars()
  request_list=[req for req in reqs]
  return jsonify(request_list)

@janitorial_bp.route('/',methods=['POST'])
@jwt_required()
def create_request():
  request_data=request.get_json()
  now=datetime.now()
  user=auth_user()
  try:
    req = Janitorial(
    rua=request_data['rua'],
    bairro=request_data['bairro'],
    area=request_data['area'],
    cep=request_data['cep'],
    servico=request_data['servico'],
    desc=request_data['desc'],
    anexo=request_data['anexo'],
    protocolo=request_data['protocolo'],
    data=now.strftime('%d/%m/%Y'),
    hora=now.strftime('%H:%M:%S'),
    user_id=user.id
    )
    db.session.add(req)
    db.session.commit()
    print(user.nome)
  except Exception as e:
    return jsonify({'error':str(e)})
  return jsonify({'response':'servico solicotado'})

@janitorial_bp.route('/<int:id>',methods=['GET'])
@jwt_required()
def get_request(id):
  try:
    request=db.get_or_404(Janitorial,id)
  except Exception as e:
    return jsonify({'response:':str(e)}),404
  return jsonify(request)

@janitorial_bp.route('/<int:id>',methods=['PUT'])
@jwt_required()
def update_request(id):
  request_data=request.get_json()
  try:
    req=db.get_or_404(Janitorial,id)
    req.rua=request_data['rua']
    req.bairro=request_data['bairro']
    req.area=request_data['area']
    req.cep=request_data['cep']
    req.servico=request_data['servico']
    req.desc=request_data['desc']
    req.anexo=request_data['anexo']
    req.protocolo=request_data['protocolo']
    db.session.add(req)
    db.session.commit()
  except Exception as e:
    return jsonify({'response':str(e)})
  return jsonify({'response':'solicitacao alterada'})
  
@janitorial_bp.route('/<int:id>',methods=['DELETE'])
@jwt_required()
def delete_request(id):
  try:
    req=db.get_or_404(Janitorial,id)
    db.session.delete(req)
    db.session.commit()
  except Exception as e:
    return jsonify({'response':str(e)})
  return jsonify({'response':'solicitacao excluida'})