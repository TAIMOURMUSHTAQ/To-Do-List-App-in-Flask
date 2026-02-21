#app init
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#Create database object globally
db=SQLAlchemy()

#Function to create flask app,  app factory functions
def create_app():
    #main engine
    app=Flask(__name__)

    #configuration settings
    #For sessions/cookies
    app.config['SECRET_KEY']='my-secret-key'
    #For db connections
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///todo.db'
    #Track modification
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

    #Db connection with app
    db.init_app(app)

    #they are like mini modules having relative routes to inform flask about them
    from app.routes.auth import auth_bp
    from app.routes.tasks import tasks_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)

    return app