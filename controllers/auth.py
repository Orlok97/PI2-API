from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from database import db
from database.models import User, Admin, Employee

auth_bp=Blueprint('auth_bp',__name__)

def auth_user():
  return User.query.filter_by(email=get_jwt_identity()).first()
  
def auth(email,senha,model):
  user_model=model.query.filter_by(email=email).first()
  if senha==user_model.senha:
    return True

@auth_bp.route('/',methods=['POST'])
def login():
  request_data=request.get_json()
  model=None
  email=request_data['email']
  senha=request_data['senha']
  permission=request_data['permission']
  if permission == 'admin':
    model=Admin
  elif permission =='citizen':
    model=User
  elif permission == 'employee':
    model=Employee
    
  if auth(email,senha,model):
    token=create_access_token(identity=email)
    return jsonify({
      "response":"usuario autenticado",
      'token':token,
      'status':'ok',
      'permission':permission
    })
  else:
    return jsonify({'response':'erro na autenticação',
                    'status':'error'})
  
@auth_bp.route('/citizen',methods=['GET'])
@jwt_required()
def get_auth_citizen():
  user_email=get_jwt_identity()
  user=db.session.execute(db.select(User).filter_by(email=user_email)).scalar_one()
  return jsonify(user)
  
@auth_bp.route('/admin',methods=['GET'])
@jwt_required()
def get_auth_admin():
  user_email=get_jwt_identity()
  user=db.session.execute(db.select(Admin).filter_by(email=user_email)).scalar_one()
  return jsonify(user)

@auth_bp.route('/employee',methods=['GET'])
@jwt_required()
def get_auth_employee():
  user_email=get_jwt_identity()
  user=db.session.execute(db.select(Employee).filter_by(email=user_email)).scalar_one()
  return jsonify(user)
