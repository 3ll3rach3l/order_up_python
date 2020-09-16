from flask import Flask
from .config import Configuration
from .models import db, Employee #import the db variable from models module
from .routes import orders, session
from flask_login import LoginManager 

''' 
In the app/__init__.py file, bootstrap (that means "declare and configure") your
Flask app with the Blueprint from app.routes.order and the configuration object.
This time, give relative imports a try. (See them, there?)
'''
app = Flask(__name__)
app.config.from_object(Configuration)
app.register_blueprint(orders.bp)
app.register_blueprint(session.bp)
db.init_app(app)  # Configure the application with SQLAlchemy passing in the app variable

login = LoginManager(app)  #create the login manager for app to protect routes
login.login_view = 'session.login' #instructs login mgr to use "session.login" Blueprint function

@login.user_loader #configs LoginManger to use load_user func to get employee objects from database
def load_user(id):
    return Employee.query.get(int(id))