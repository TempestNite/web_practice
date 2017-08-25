from flask import Flask
from flask_recaptcha import ReCaptcha
app = Flask(__name__, template_folder='../templates', static_folder='../static')
recaptcha = ReCaptcha(app=app)

app.secret_key = 'super secret key'

import webapp.routes
