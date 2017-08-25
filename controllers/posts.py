from flask import Blueprint, render_template, session
from libraries.posts import Posts

# controller for default / url prefix
posts = Blueprint("posts",__name__,template_folder="templates")

# Main view that shows index.html
@posts.route("/",methods=["GET"])
def all_userposts():
	return render_template("userposts.html")
	
@posts.route("/user",methods=["GET"])
def user_posts():
    posts_obj = Posts()
    param_list = posts_obj.userposts()
    return render_template("userposts.html", userposts = param_list)

@posts.route("/make",methods=["GET"])
def make_post():
	return render_template("makepost.html")