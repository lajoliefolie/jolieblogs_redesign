from flask import Blueprint, render_template, session, request, jsonify
from libraries.userhandler import Userhandler

# controller for default / url prefix
login = Blueprint("login",__name__,template_folder="templates")

# Main view that shows index.html
@login.route("/",methods=["GET","POST"])
def login_view():
    return render_template("login.html")
    
@login.route("/process",methods=["GET"])
def login_process():
    userhandler = Userhandler()
    valid_login = userhandler.login(email = request.args.get("email"), password = request.args.get("password"))
    return jsonify(valid_login)