UPLOAD_FOLDER = '/portal-zeladoria/PI2-API/uploads/'

class Config:
  def __init__(self, app):
    self.app=app
    self.configure()
  def configure(self):
    self.app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///zeladoria.db"
    self.app.config["JWT_SECRET_KEY"]="HDJDUDJSJJDJDUJDJDU73JE8DJ39W02Khdje7"
    self.app.json.sort_keys = False
    self.app.config['JSON_AS_ASCII'] = False
    self.app.config["JSONIFY_MIMETYPE"] = "application/json; charset=utf-8"
    self.app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
    print('app configurado')