from flask import Flask
import os

app = Flask(__name__)

# Importing controllers
from controllers.homepage import homepage
app.register_blueprint(homepage, url_prefix='/')


if __name__ == "__main__":
    # Starting with these values due to c9.io
    host = os.getenv("IP", "0.0.0.0")
    port = os.getenv("PORT", 8080)
    app.secret_key='teststring' # Oh, hush
    app.run(host, port)