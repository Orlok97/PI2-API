from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from database import db
from database.models import Employee

employee_bp=Blueprint('employee_bp',__name__)

@employee_bp.route('/',methods=['GET'])
#@jwt_required()
def list_employees():
  employees=db.session.execute(db.select(Employee).order_by(Employee.id)).scalars()
  employee_list=[e for e in employees]
  return jsonify(employee_list)

@employee_bp.route('/',methods=['POST'])
@jwt_required()
def create_employee():
  request_data=request.get_json()
  try:
    employee=Employee(
    nome=request_data['nome'],
    email=request_data['email'],
    senha=request_data['senha'],
    cargo=request_data['cargo']
      )
    db.session.add(employee)
    db.session.commit()
  except Exception as e:
    db.session.rollback()
    return jsonify({
      'error':str(e)
    })
  return jsonify({
    'response':'funcionario cadastrado!'
  })
  
@employee_bp.route('/<int:id>',methods=['GET'])
@jwt_required()
def get_employee(id):
  try:
    employee=db.get_or_404(Employee,id)
    return jsonify(employee)
  except Exception as e:
    return jsonify({
      'response':'usuario nao encontrado.',
      'error':str(e)
    })
    
@employee_bp.route('/<int:id>',methods=['PUT'])
@jwt_required()
def update_employee(id):
  request_data=request.get_json()
  try:
    employee=db.get_or_404(Employee,id)
    employee.nome=request_data['nome']
    employee.email=request_data['email']
    employee.senha=request_data['senha']
    employee.cargo=request_data['cargo']
    db.session.add(employee)
    db.session.commit()
    return jsonify({
      'response':'dados alterados com sucesso.'
    })
  except Exception as e:
    db.session.rollback()
    return jsonify({
      'response':'erro ao alterar os dados.',
      'error':str(e)
    })

@employee_bp.route('/<int:id>',methods=['DELETE'])
@jwt_required()
def delete_employee(id):
  try:
    employee=db.get_or_404(Employee,id)
    db.session.delete(employee)
    db.session.commit()
    return jsonify({
      'response':'funcionario excluido.'
    })
  except Exception as e:
    return jsonify({
      'response':'erro ao excluir o funcionario.',
      'error':str(e)
    })