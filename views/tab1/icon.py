#coding:utf-8

from flask import Blueprint, render_template ,request
import re

icon = Blueprint('icon', __name__)

##########################################
#   【视图类型】访问tab1中icons类别
##########################################
@icon.route('/')
def index():
    #获取请求的路劲
    url = request.url
    reqPath = re.findall("http://(.*)$",url)[0]
    reqPath = re.findall("/(.*)$", reqPath)[0]
    arg = {}

    path = "tab1/icon_index.html"
    arg["path"] = reqPath.split("/")
    return render_template(path,arg=arg)