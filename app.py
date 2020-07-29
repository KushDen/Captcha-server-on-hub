from flask import Flask, request, redirect, url_for, render_template, send_file
from werkzeug.utils import secure_filename
from PIL import Image
import os
import numpy as np
from showResultYandex import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload():
    return render_template('upload.html')

@app.route('/download/', methods=['POST'])
def download():

    try:
        image = request.files['fileToUpload']
        nom_image = secure_filename(image.filename)
        image = Image.open(image)
        #image = np.array(image)
        #image.save('/home/denis/micro_server/static/images/'+nom_image)
        return show_result(image) #send_file('/home/denis/micro_server/static/images/'+nom_image, mimetype='image/jpeg', attachment_filename=nom_image, as_attachment=True)

    except Exception as e:
        print(e)
        return redirect(url_for('upload'))
    
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
