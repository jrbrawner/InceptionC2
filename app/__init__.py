import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import logging
from .Classes.Server import Server
import secrets

### Source code base directory
basedir = os.path.abspath(os.path.dirname(__file__))

#Instantiate database object
db = SQLAlchemy()

def create_app():
    """Construct core app object."""
    server = Server('Inception')
    
    app = Flask(__name__, template_folder='templates')

    #Setting up configuration
    app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'development.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config['SECRET_KEY'] = secrets.token_urlsafe(16)

    logging.basicConfig(filename='record.log',level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s : %(message)s', filemode='w+')
    
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s')
    console.setFormatter(formatter)
    logging.getLogger("").addHandler(console)

    #Initialize plugins
    db.init_app(app)
   
    with app.app_context():
        
        from .routes.app_route import app_bp

        #register blueprints with app
        app.register_blueprint(app_bp)
        
        #instantiate database tables
        db.create_all()
        

    return app

   






    
    
