from flask import Flask
from flask_recaptcha import ReCaptcha
app = Flask(__name__)
recaptcha = ReCaptcha(app=app)

app.secret_key = 'super secret key'
app.run(debug=True)

