from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base


app = Flask(__name__)



# Importing Database
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/brainbloomDatabase'
db.init_app(app)

Base = automap_base()
Base.prepare(db.engine, reflect=True)

# Initialise Tables
User = Base.classes.user

# Registering blueprints
from routes.shared import shared_view
from routes.user import user_view
from routes.staff import staff_view

app.register_blueprint(shared_view)
app.register_blueprint(user_view, url_prefix='/user')
app.register_blueprint(staff_view, url_prefix='/staff')


if __name__ == '__main__':
    app.run(debug=True)