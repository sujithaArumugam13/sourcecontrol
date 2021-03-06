
from flask import Flask, request, render_template, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_folder='static', template_folder='static')
CORS(app)
app.config['UPLOAD_EXTENSIONS'] = ['.csv', '.xlsx', '.xls', '.json', '.xml']
app.config['MAX_CONTENT_LENGTH'] = 10000* 1024 * 1024

@app.route("/")
def helloWorld():
  return render_template('index.html')

@app.route("/static/")
def helloWorld1():
  return render_template('index.html')



@app.route('/classify_cols',methods=['GET'])
def classify_cols():
    jsonString="testting"
    return jsonString



@app.route('/classify_cols_v1',methods=['GET'])
def classify_cols():
    jsonString=""
    return jsonString


@app.route('/classify_cols_v2',methods=['GET'])
def classify_cols():
    jsonString=""
    return jsonString


#Test changes
@app.route('/classify_cols_v4',methods=['GET'])
def classify_col_ius():
    jsonString=""
    return jsonString