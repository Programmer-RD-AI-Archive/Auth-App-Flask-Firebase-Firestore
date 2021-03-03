from flask import *

app = Flask(__name__)
app.debug = True
app.secret_key = "RANUGA D 2008"
from server.routes import *