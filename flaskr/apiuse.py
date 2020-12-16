from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from flaskr.auth import login_required
import requests

bp = Blueprint('sound', __name__, url_prefix='/sound')


@bp.route('/display')
@login_required
def display_page():

    r = requests.get('https://api.chucknorris.io/jokes/random')
    r_json = r.json()

    whatever = r_json['value']



    return render_template('sound/display.html', randomJoke=whatever, img=r_json['icon_url'])
