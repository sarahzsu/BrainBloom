from flask import Blueprint, render_template, redirect, url_for

user_view = Blueprint('user_routes', __name__, template_folder='../templates/user', static_folder='../static')

@user_view.route("/")
def home():
    return render_template('userhome.html')
