import secrets
import os
import sys
from flask import Flask, send_from_directory
from flask_cors import CORS

import models  # Import the models directory to create schema on MySQL DB.
from config import *  # Flask App Config
from controllers import *
from extensions import db

URI = 'mysql+pymysql://{0}:{1}@{2}:{3}/{4}'.format(USER, PASSWORD, HOST, PORT, SCHEMA)


# Function to create blueprints and initialise db
def register_extensions(app_obj):
    app_obj.app_context().push()
    app_obj.register_blueprint(user_controller, url_prefix="/api/users")
    app_obj.register_blueprint(project_controller, url_prefix="/api/projects")
    db.init_app(app_obj)
    db.create_all()


# Function to configure database with Flask
def create_app(name):
    app_obj = Flask(name, static_folder='frontend/build')
    app_obj.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DB_CONN")     #Link to connect db: 'mysql+pymysql://root:toor@localhost:3306/ase'
    app_obj.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app_obj.secret_key = os.getenv("SECRET_KEY")
    register_extensions(app_obj)
    CORS(app_obj)

    return app_obj

app = create_app(__name__)

# Serve React Static Assets
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=os.environ.get('PORT', 5000))
