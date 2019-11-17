from logging import getLogger

from flask import Blueprint, redirect, render_template, request

from app.dbModels import CSVtoDB, commit, stop

case2 = Blueprint('ex2', __name__,  url_prefix='/ex2')

LOG = getLogger(__name__)

@case2.route('/')
def index():
    return render_template("uploadCSV.html", case = 2)

@case2.route('/upload', methods = ['POST'])
def upload():
    """
    API Endpoint to upload the CSV file. It provides a form in which the file to the uploaded can be 
    selected and added to the respective database. 
    """
    try:
        csvFile = request.files.get('data', None)
        fileName = csvFile.filename
    except:
        LOG.error("File Not Found!")
        return redirect("/ex2")        
    
    try:
        CSVtoDB(2, fileName)
    except Exception as e:
        LOG.error(e)
        LOG.error("Invalid operation!")
        return redirect('/ex2')

    return render_template("uploadComplete.html", case = 2)

@case2.route('/stopUpload', methods=['GET'])
def stopUpload():
    """
    API Endpoint to stop the upload process. If the stop request is sent before the upload process is complete, the changes made will be 
    rolled back and will not be commited to the database. 
    """
    
    stop()
    return render_template("uploadStopped.html", case = 2)

@case2.route('/pauseUpload', methods=['GET'])
def pauseUpload():
    pass

@case2.route('/resumeUpload', methods=['GET'])
def resumeUpload():
    pass
