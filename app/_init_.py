from flask import Flask
from .config import DevConfig

# Initializing application
app = Flask(__name__,instance_relative_config = True)

# Setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

from app import views
from flask_bootstrap import Bootstrap

# Initializing application
app = Flask(__name__,instance_relative_config = True)

# Setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile("config.py")

# Initializing Flask Extensions
bootstrap = Bootstrap(app)

from app import views
from app import error

from flask import Flask
from flask_bootstrap import Bootstrap
from .config import config_opions

bootstrap = Bootstrap()

def create_app(config_name):

    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object (config_option[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)

    # Will add the views and forms

    return app

def create_app(config_name):
    #....
    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # setting config
    from .request import configure_request
    configure_request(app)

    return app
from flask import Flask
from flask_bootstrap import Bootstrap
from .config import config_options

bootstrap = Bootstrap()

def create_app(config_name):

    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)

    # Will add the views and forms

    return app

