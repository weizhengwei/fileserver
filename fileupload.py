from flask import Flask
from flask import request, render_template
import os

app = Flask(__name__)
SAVEPATH = os.path.curdir+'/file/'

@app.route('/')
def index():
	return render_template('upload.html')

@app.route('/upload', methods=['GET','POST'])
def upload():
	if request.method == 'GET':
		return render_template('upload.html')
	elif request.method == 'POST':
		return uploadfile(request)

def uploadfile(req):
	file = req.files['filename']
	filename = file.filename
	file.save(SAVEPATH+filename)
	return '%s save success' % filename

if __name__ == '__main__':
	app.run(debug=True, port=8888)