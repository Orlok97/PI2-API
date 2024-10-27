from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from config import Config
from database import db

from controllers.user import citizen_bp
from controllers.janitorial import janitorial_bp
from controllers.employee import employee_bp
from controllers.service import service_bp
from controllers.admin import admin_bp
from controllers.auth import auth_bp

app=Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

config=Config(app)
jwt=JWTManager(app)

db.init_app(app)
with app.app_context():
    db.create_all()

@app.route('/',methods=['GET'])
@app.route('/api/',methods=['GET'])
@app.route('/api/v1/',methods=['GET'])
def api_description():
  return jsonify({
    'name':'portal-zeladoria',
    'version':'1.0.0',
    'description':'API para solicitar e gerenciar serviços da prefeitura de São Vicente.'
  })
  
app.register_blueprint(auth_bp,
url_prefix='/api/v1/auth')
app.register_blueprint(citizen_bp,
url_prefix='/api/v1/citizen')
app.register_blueprint(janitorial_bp,
url_prefix='/api/v1/janitorial')
app.register_blueprint(employee_bp,
url_prefix='/api/v1/employee')
app.register_blueprint(service_bp,
url_prefix='/api/v1/service')
app.register_blueprint(admin_bp,
url_prefix='/api/v1/admin')

if __name__ == '__main__':
  app.run(debug=True)