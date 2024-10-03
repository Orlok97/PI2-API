UPLOAD_FOLDER = 'uploads/'
class Config:
  def __init__(self, app):
    self.app=app
    self.configure()
  def configure(self):
    self.app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///zeladoria.db"
    self.app.config["JWT_SECRET_KEY"]="HDJDUDJSJJDJDUJDJDU73JE8DJ39W02Khdje7"
    self.app.json.sort_keys = False
    print('app configurado')
    self.app.config["UPLOAD_FOLDER"] ='uploads/'   