from flask import Blueprint

from extensions import db

home_controller = Blueprint("controllers/home_controller",
                            __name__, static_folder="static", template_folder="templates")


# @home_controller.route('/', methods=['GET'])
# def home():
#     try:
#         tables = db.engine
#         return '<h1>Connected to database</h1><h3>The database engine is: {}</h3>'.format(tables)
#     except:
#         return '<h1>Something is broken.</h1>'

# Production build files for React
@home_controller.route('/', methods=["GET"])
def index():
    return home_controller.send_static_file('index.html')

# Client Side Routing
@home_controller.errorhandler(404)
def not_found(e):
    return home_controller.send_static_file('index.html')