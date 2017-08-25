from flask import Blueprint, render_template, session

# controller for default / url prefix
homepage = Blueprint("homepage",__name__,template_folder="templates")

# Main view that shows index.html
@homepage.route("/",methods=["GET"])
def homepage_view():
    
	return render_template("homepage.html")