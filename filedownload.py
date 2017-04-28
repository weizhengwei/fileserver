from flask import Flask
from flask.ext.autoindex import AutoIndex
import os

app = Flask(__name__)
AutoIndex(app, os.path.curdir+'/file')

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=9999)