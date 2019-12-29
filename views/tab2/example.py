#coding:utf-8

from flask import Blueprint, render_template ,request
import re

example = Blueprint('example', __name__)

##########################################
#   【视图类型】访问tab2中的example页面
##########################################
@example.route('/')
def index():
    #获取请求的路劲
    url = request.url
    reqPath = re.findall("http://(.*)$",url)[0]
    reqPath = re.findall("/(.*)$", reqPath)[0]
    arg = {}

    path = "tab2/example.html"
    arg["path"] = reqPath.split("/")
    return render_template(path,arg=arg)