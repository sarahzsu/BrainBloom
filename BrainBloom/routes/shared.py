from flask import Blueprint, render_template, redirect, url_for, current_app
from sqlalchemy.ext.automap import automap_base

shared_view = Blueprint('shared_routes', __name__, template_folder='../templates', static_folder='../static')




@shared_view.route("/")
def home():
    with current_app.app_context():
        db = current_app.extensions['sqlalchemy'].db
        Base = automap_base()
        Base.prepare(db.engine, reflect=True)
        
        User = Base.classes.user
        results = db.session.query(User)
        for r in results:
            print(r.username)
    return render_template('landing/landingpage.html')
