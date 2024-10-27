from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from database import db
from database.models import Service

service_bp=Blueprint('service_bp',__name__)

@service_bp.route('/',methods=['GET'])
@jwt_required()
def list_services():
  services= db.session.execute(db.select(Service).order_by(Service.id)).scalars()
  service_list = [service for service in services]
  return jsonify(service_list)

@service_bp.route('/',methods=['POST'])
@jwt_required()
def create_service():
  request_data=request.get_json()
  try:
    service=Service(
      nome=request_data['nome'],
      desc=request_data['desc']
      )
    db.session.add(service)
    db.session.commit()
    return jsonify({
      'response':'serviço cadastrado com sucesso.'
    })
  except Exception as e:
    db.session.rollback()
    return jsonify({
      'response':'erro ao cadastrar o serviço',
      'error':str(e)
    })

@service_bp.route('/<int:id>',methods=['GET'])
@jwt_required()
def get_service(id):
  try:
    service=db.get_or_404(Service,id)
    return jsonify(service)
  except Exception as e:
    return jsonify({
      'response':'serviço não encontrado.',
      'error':str(e)
    })

@service_bp.route('/<int:id>',methods=['PUT'])
@jwt_required()
def update_service(id):
  request_data=request.get_json()
  try:
    service=db.get_or_404(Service,id)
    service.nome=request_data['nome']
    service.desc=request_data['desc']
    db.session.add(service)
    db.session.commit()
    return jsonify({
        'response':'serviço alterado com sucesso'
      })
  except Exception as e:
    return jsonify({
      'response':'serviço não encontrado',
      'error':str(e)
    })

@service_bp.route('/<int:id>',methods=['DELETE'])
@jwt_required()
def delete_services(id):
  try:
    service=db.get_or_404(Service,id)
    db.session.delete(service)
    db.session.commit()
    return jsonify({
      'response':'serviço deletado com sucesso.'
    })
  except Exception as e:
    return jsonify({
      'response':'erro ao deletar o registro',
      'error':str(e)
    })