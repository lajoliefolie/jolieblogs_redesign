from flask import Flask
import os
from flask_login import LoginManager
from libraries.userhandler import Userhandler

app = Flask(__name__)

# Importing controllers
from controllers.homepage import homepage
from controllers.posts import posts
from controllers.login import login
from controllers.logout import logout
from controllers.register import register

app.register_blueprint(homepage, url_prefix='/')
app.register_blueprint(posts, url_prefix='/posts')
app.register_blueprint(login, url_prefix='/login')
app.register_blueprint(logout, url_prefix='/logout')
app.register_blueprint(register, url_prefix='/register')

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login.login_view"

@login_manager.user_loader
def load_user(email):
    user = Userhandler()
    return user.get(email = email)

if __name__ == "__main__":
    # Starting with these values due to c9.io
    host = os.getenv("IP", "0.0.0.0")
    port = os.getenv("PORT", 8080)
    app.secret_key='teststring' # Oh, hush
    app.run(host, port)