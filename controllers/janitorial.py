import os
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from database import db
from database.models import Janitorial
from controllers.auth import auth_user
from datetime import datetime
from werkzeug.utils import secure_filename
from config import UPLOAD_FOLDER

janitorial_bp = Blueprint('janitorial_bp', __name__)

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def janitorial_to_dict(janitorial):
    return {
        'id': janitorial.id,
        'rua': janitorial.rua,
        'bairro': janitorial.bairro,
        'area': janitorial.area,
        'cep': janitorial.cep,
        'servico': janitorial.servico,
        'desc': janitorial.desc,
        'anexo': janitorial.anexo,
        'protocolo': janitorial.protocolo,
        'data': janitorial.data,
        'hora': janitorial.hora,
        'user_id': janitorial.user_id
    }

@janitorial_bp.route('/', methods=['GET'])
@jwt_required()
def get_requests():
    reqs = db.session.execute(db.select(Janitorial).order_by(Janitorial.id)).scalars()
    request_list = [janitorial_to_dict(req) for req in reqs]
    return jsonify(request_list)

@janitorial_bp.route('/', methods=['POST'])
@jwt_required()
def create_request():
    request_data = request.form.to_dict()
    now = datetime.now()
    user = auth_user()

    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)


        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)

        file.save(os.path.join(UPLOAD_FOLDER, filename))
    else:
        filename = ''

    try:
        req = Janitorial(
            rua=request_data['rua'],
            bairro=request_data['bairro'],
            area=request_data['area'],
            numero=request_data['numero'],
            cep=request_data['cep'],
            servico=request_data['servico'],
            desc=request_data['desc'],
            anexo=filename,
            protocolo=request_data['protocolo'],
            data=now.strftime('%d/%m/%Y'),
            hora=now.strftime('%H:%M:%S'),
            user_id=user.id
        )
        db.session.add(req)
        db.session.commit()
        print(user.nome)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

    return jsonify({'response': 'Serviço solicitado'}), 200

@janitorial_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
def get_request(id):
    try:
        janitorial_request = db.get_or_404(Janitorial, id)
    except Exception as e:
        return jsonify({'response': str(e)}), 404
    return jsonify(janitorial_to_dict(janitorial_request))

@janitorial_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_request(id):
    request_data = request.get_json()
    try:
        req = db.get_or_404(Janitorial, id)
        req.rua = request_data['rua']
        req.bairro = request_data['bairro']
        req.area = request_data['area']
        req.cep = request_data['cep']
        req.servico = request_data['servico']
        req.desc = request_data['desc']
        req.anexo = request_data['anexo']
        req.protocolo = request_data['protocolo']
        db.session.add(req)
        db.session.commit()
    except Exception as e:
        return jsonify({'response': str(e)}), 400
    return jsonify({'response': 'Os Dados da Solicitação foram alterados'})

@janitorial_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_request(id):
    try:
        req = db.get_or_404(Janitorial, id)
        db.session.delete(req)
        db.session.commit()
    except Exception as e:
        return jsonify({'response': str(e)}), 400
    return jsonify({'response': 'Solicitação excluída'})