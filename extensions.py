import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from config import *
from sqlalchemy.orm import sessionmaker,scoped_session
import os

# url = 'mysql+pymysql://{0}:{1}@{2}'.format(USER, PASSWORD, HOST)
url = os.getenv("DB_URL")
engine = sqlalchemy.create_engine(url)  # connect to server
engine.execute("CREATE SCHEMA IF NOT EXISTS `{0}`;".format(os.getenv("SCHEMA")))    # create 'ase' schema if it does not exist
engine.execute("USE {0};".format(os.getenv("SCHEMA")))  # select new 'ase' schema

db = SQLAlchemy()
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


# from sqlalchemy.orm import scoped_session
# import threading
# from models import *
# from extensions import db, Session
#
# def run():
#     threading.Thread(target=task).start()
#     print("The main run function has returned")
#     return
#
# def task():
#     print(f"Task has started on {threading.current_thread().name}")
#     sess = Session()
#     print(f"Example query of users: {sess.query(User).filter_by(username='cs').first()}")
#     print("Task has ended")
#     Session.remove()