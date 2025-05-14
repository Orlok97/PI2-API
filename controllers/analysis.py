from flask import Blueprint, request, jsonify
from database import db
from database.models import Janitorial, Analysis

analysis_bp=Blueprint('analysis_bp',__name__)

@analysis_bp.route('/', methods=['GET'])
def get_all_requests():
   results=db.session.query(Analysis, Janitorial).join(Janitorial).filter(Analysis.janitorial_id == Janitorial.id).all()
   data=[{
      'id_usuario':janitorial.user_id,
      'nome_solicitante':janitorial.user_name,
      'data_solicitacao':analysis.data_solicitacao,
      'data_finalizacao':analysis.data_finalizado,
      'hora_solicitcao':analysis.hora_solicitacao,
      'hora_servico_finalizacao':analysis.hora_finalizado,
      'bairro':janitorial.bairro,
      'cep':janitorial.cep
      } for analysis, janitorial in results]
   return jsonify(data)

@analysis_bp.route('/<int:id>', methods=['GET'])
def get_data_request(id):
   analysis=db.get_or_404(Analysis,id)
   janitorial=db.session.query(Janitorial).filter(Janitorial.id == analysis.janitorial_id).first()
   data={
      'id_usuario':janitorial.user_id,
      'nome_solicitante':janitorial.user_name,
      'data_solicitacao':analysis.data_solicitacao,
      'data_finalizacao':analysis.data_finalizado,
      'hora_solicitcao':analysis.hora_solicitacao,
      'hora_servico_finalizado':analysis.hora_finalizado,
      'bairro':janitorial.bairro,
      'cep':janitorial.cep
      }
   return jsonify(data)