import os
from werkzeug.utils import secure_filename
from config import UPLOAD_FOLDER

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    
def upload(file,folder=''):
  try:
    if file and allowed_file(file.filename):
      filename = secure_filename(file.filename)
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