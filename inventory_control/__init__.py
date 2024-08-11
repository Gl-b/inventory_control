from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = ':^)'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:root@localhost/inventorydb'
csrf = CSRFProtect(app)
db = SQLAlchemy(app)

from inventory_control import routes