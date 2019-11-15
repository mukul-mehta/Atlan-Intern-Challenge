from flask import Blueprint, request, redirect, render_template

from app import dbModels

case3 = Blueprint('ex3', __name__,  url_prefix='/ex3')


