import os
from datetime import timedelta
from dotenv import load_dotenv

UPLOAD_FOLDER = 'portal-zeladoria/PI2-API/uploads/'
load_dotenv()

class Config:
  def __init__(self, app):
    self.app=app
    self.configure()
  def configure(self):
    self.app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('DATABASE_URI')
    self.app.config["JWT_SECRET_KEY"]=os.getenv('SECRET_KEY')
    self.app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
    self.app.json.sort_keys = False
    self.app.config['JSON_AS_ASCII'] = False
    self.app.config["JSONIFY_MIMETYPE"] = "application/json; charset=utf-8"
    self.app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
    print('app configurado')