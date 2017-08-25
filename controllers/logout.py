from flask import Blueprint, render_template, session
from libraries.userhandler import Userhandler

# controller for default / url prefix
logout = Blueprint("logout",__name__,template_folder="templates")

# Main view that shows index.html
@logout.route("/",methods=["GET"])
def logout_view():
	return render_template("login.html")