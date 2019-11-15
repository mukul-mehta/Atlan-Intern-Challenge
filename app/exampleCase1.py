import io
import time
from flask import Blueprint, request, redirect, render_template
from logging import getLogger
from app.dbModels import CSVtoDB, stop, commit

case1 = Blueprint('ex1', __name__,  url_prefix='/ex1')

LOG = getLogger(__name__)

@case1.route('/')
def index():
    return render_template("uploadCSV.html")

@case1.route('/upload', methods = ['POST'])
def upload():
    try:
        csvFile = request.files.get('data', None)
        fileName = csvFile.filename
    except:
        LOG.error("File Not Found!")
        return redirect("/ex1")
    
    try:
        CSVtoDB(1, fileName)
    except Exception as e:
        LOG.error(e)
        LOG.error("Invalid operation!")
        return redirect('/ex1')

    return render_template("uploadComplete.html")

@case1.route('/stopUpload', methods=['GET'])
def stopUpload():
    stop()
    return render_template("uploadStopped.html")