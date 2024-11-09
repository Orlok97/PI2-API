import os
import uuid
from werkzeug.utils import secure_filename
from config import UPLOAD_FOLDER

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    
def generate_new_filename(filename):
  extension=filename.rsplit('.',1)[1].lower()
  new_filename=uuid.uuid4().hex
  return f"{new_filename}.{extension}"
  
def upload(file,folder=''):
  try:
    if file and allowed_file(file.filename):
      filename = generate_new_filename(file.filename)
      if not os.path.exists(UPLOAD_FOLDER+folder):
        os.makedirs(UPLOAD_FOLDER+folder)
      file.save(os.path.join(UPLOAD_FOLDER+folder, filename))
      print('upload feito com sucesso')
      return filename
    else:
      return None
  except Exception as e:
    print('erro:',e)
    return None