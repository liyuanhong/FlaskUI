from flask import Blueprint, render_template, Response ,request

other = Blueprint('other', __name__)

@other.route('/')
def index():
    path = "other/index.html"
    arg = {}
    arg["path"] = path.split("/")
    return render_template(path,arg=arg)