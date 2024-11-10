from controllers.citizen import citizen_bp
from controllers.janitorial import janitorial_bp
from controllers.employee import employee_bp
from controllers.service import service_bp
from controllers.admin import admin_bp
from controllers.auth import auth_bp
from controllers.uploads import uploads_bp

class Router:
  def __init__(self,app):
    self.app=app
    self.routes()
  def routes(self):
    self.app.register_blueprint(auth_bp,
    url_prefix='/api/v1/auth')
    self.app.register_blueprint(citizen_bp,
    url_prefix='/api/v1/citizen')
    self.app.register_blueprint(janitorial_bp,
    url_prefix='/api/v1/janitorial')
    self.app.register_blueprint(employee_bp,
    url_prefix='/api/v1/employee')
    self.app.register_blueprint(service_bp,
    url_prefix='/api/v1/service')
    self.app.register_blueprint(admin_bp, url_prefix='/api/v1/admin')
    self.app.register_blueprint(uploads_bp,
    url_prefix='/uploads')