from flask import Blueprint, render_template, session, request, jsonify
from libraries.userhandler import Userhandler

# controller for default / url prefix
register = Blueprint("register",__name__,template_folder="templates")

# Main view that shows index.html
@register.route("/",methods=["GET"])
def register_view():
	return render_template("register.html")
	
@register.route("/process",methods=["GET"])
def register_process():
    userhandler = Userhandler()
    register_code = userhandler.register(email = request.args.get("email"), 
                                        password = request.args.get("password"),
                                        password_confirm = request.args.get("password_confirm"))
    return jsonify(register_code)