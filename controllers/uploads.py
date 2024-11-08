from flask import Blueprint, send_from_directory
from config import UPLOAD_FOLDER

uploads_bp=Blueprint('uploads_bp',__name__)

@uploads_bp.route('/anexo/<filename>',methods=['GET'])
def get_attachment(filename):
  return send_from_directory(f"{UPLOAD_FOLDER}/anexo/",filename)