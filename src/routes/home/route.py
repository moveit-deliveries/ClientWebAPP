from flask import render_template, Blueprint

home_route = Blueprint('home', __name__)


@home_route.get('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')
