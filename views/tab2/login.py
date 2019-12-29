#coding:utf-8

from flask import Blueprint, render_template ,request
import re

login = Blueprint('login', __name__)

##########################################
#   【视图类型】访问tab2首页login页面
##########################################
@login.route('/')
def index():
    #获取请求的路劲
    url = request.url
    reqPath = re.findall("http://(.*)$",url)[0]
    reqPath = re.findall("/(.*)$", reqPath)[0]
    arg = {}

    path = "tab2/login.html"
    arg["path"] = reqPath.split("/")
    return render_template(path,arg=arg)