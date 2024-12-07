import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from app.config import Config

# App instance 
db = SQLAlchemy()
migrate = Migrate( db)
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = "users.login"
login_manager.login_message_category = "info"
mail = Mail()



# Create App BluePrint 
def create_app(config_calss=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    migrate.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    
    
    from app.main.routes import main
    from app.users.routes import users
    from app.tasks.routes import tasks
    from app.errors.handlers import errors
    
    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(tasks)
    app.register_blueprint(errors)
    
    with app.app_context():
        db.create_all()
    
    return app
