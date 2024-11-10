from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from config import Config
from routes import Router
from database import db

app=Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
config=Config(app)
jwt=JWTManager(app)
router=Router(app)

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
  
if __name__ == '__main__':
  app.run(debug=True)