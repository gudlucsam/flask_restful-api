from flask_api import app
from db import db


@app.before_first_request
def create_table():
	db.create_all()
    
db.init_app(app)
