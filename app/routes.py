from flask import Blueprint, render_template
from jinja2 import TemplateNotFound

main = Blueprint('main', __name__)

@main.route('/')
def index():
    try:
        return render_template('index.html', title='Home')
    except TemplateNotFound:
        return "This page is under construction.", 404

@main.route('/projects')
def projects():
    try:
        return render_template('projects.html', title='Projects')
    except TemplateNotFound:
        return "Projects page is under construction.", 404

@main.route('/about')
def about():
    try:
        return render_template('about.html', title='About Me')
    except TemplateNotFound:
        return "About Me page is under construction.", 404

