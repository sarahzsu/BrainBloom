from flask import Blueprint, render_template, redirect, url_for

staff_view = Blueprint('staff_routes', __name__, template_folder='../templates/staff', static_folder='../static')

@staff_view.route("/")
def home():
    return render_template('staffhome.html')
