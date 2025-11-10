from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

@bp.route('/')

def index():
    return render_template('index.html')

@bp.route('/guess/<letter>')
def make_guess(letter):
    return "You tried the letter '{letter}'"

