# this is app factory we will start our project from here
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def create_app(): # this is a app factory function ye apne liye ek flask app banata hai
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'your-secret-key' # ye ek secret key hai jo app ko secure banata hai for flash messages and sessions
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db' # database ka URI hai jo SQLite database use karta hai run hone ke baad sql alchemy create ho jayega
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    db.init_app(app) # initialize the database with the app
    from app.models import Task # import the Task model here to avoid circular imports
    
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    # 👆 END OF NEW LINES 👆
    from app.routes.auth import auth_bp
    from app.routes.tasks import tasks_bp

    app.register_blueprint(auth_bp) # register the auth blueprint, means ye auth routes ko app me add kar dega
    app.register_blueprint(tasks_bp) # register the tasks blueprint means ye tasks routes ko app me add kar dega     
    return app