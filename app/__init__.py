from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from .main import main as main_blueprint
from flask_script import Manager


bootstrap = Bootstrap()
db = SQLAlchemy()
def create_app(config_name):
    
    app = Flask(__name__)
    db.init_app(app)
    
    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)

    # Registering the blueprint
  
    app.register_blueprint(main_blueprint)


    #setting config
    
    # configure_request(app)

    return app