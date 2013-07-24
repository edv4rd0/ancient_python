from flask import Flask, session
from flask.ext.pymongo import PyMongo

SALT = 'c7425a7bec3f446493a08bf6f1bed422'

app = Flask(__name__)
app.secret_key = "SECRET" # Yeah, I know

mongo = PyMongo(app)

import python_challenge.views
