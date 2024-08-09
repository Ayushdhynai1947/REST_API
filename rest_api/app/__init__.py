from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from app.utils.config.config_client import ConfigClient

db = SQLAlchemy()
api = Api()

def create_app():
    app = Flask(__name__)
    
    # Configuration for SQLite database
    config_client = ConfigClient(env='dev')
    app.config['SQLALCHEMY_DATABASE_URI'] = config_client.get_value('database', 'ur1')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

    db.init_app(app)
    api.init_app(app)
    
    from app.routes.example_route import example_route
    app.register_blueprint(example_route, url_prefix='/api')
    
    with app.app_context():
        try:
            db.create_all()
            print("Database tables created successfully.")
        except Exception as e:
            print(f"Error creating database tables: {e}")
    
    
    
    return app
