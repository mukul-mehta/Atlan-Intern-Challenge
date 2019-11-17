from flask import Blueprint, request, redirect, render_template
from logging import getLogger

case2 = Blueprint('ex2', __name__,  url_prefix='/ex2')

LOG = getLogger(__name__)

@case2.route('/')
def index():
    return render_template("uploadCSV.html")