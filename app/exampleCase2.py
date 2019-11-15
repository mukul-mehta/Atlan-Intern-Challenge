from flask import Blueprint, request, redirect, render_template

from app import dbModels

case2 = Blueprint('ex2', __name__,  url_prefix='/ex2')


