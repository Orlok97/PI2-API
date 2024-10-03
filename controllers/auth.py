from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from database import db
from database.models import User

auth_bp=Blueprint('auth_bp',__name__)

def auth_user():

  return db.session.execute(db.select(User).filter_by(email=get_jwt_identity())).scalar()
  
def auth(email,senha):
  user=db.session.execute(db.select(User).filter_by(email=email)).scalar_one()
  if senha==user.senha:
    return True

@auth_bp.route('/',methods=['POST'])
def login():
  request_data=request.get_json()
  email=request_data['email']
  senha=request_data['senha']
  if auth(email,senha):
    token=create_access_token(identity=email)
    return jsonify({
      "response":"usuario autenticado",
      'token':token,
      'status':'ok'
    })
  else:
    return jsonify({'response':'erro na autenticacao',
                    'status':'error'})
  
@auth_bp.route('/user',methods=['GET'])
@jwt_required()
def get_auth_user():
  user_email=get_jwt_identity()
  user=db.session.execute(db.select(User).filter_by(email=user_email)).scalar_one()
  return jsonify(user)