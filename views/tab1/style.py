#coding:utf-8

from flask import Blueprint, render_template ,request
import re

style = Blueprint('style', __name__)

##########################################
#   【视图类型】访问tab1首页buttons
##########################################
@style.route('/')
def index():
    #获取请求的路劲
    url = request.url
    reqPath = re.findall("http://(.*)$",url)[0]
    reqPath = re.findall("/(.*)$", reqPath)[0]
    arg = {}

    path = "tab1/style_buttons.html"
    arg["path"] = reqPath.split("/")
    return render_template(path,arg=arg)

##########################################
#   【视图类型】访问tab1中的labels标签页面
##########################################
@style.route('/labels')
def getLabelsPage():
    #获取请求的路劲
    url = request.url
    reqPath = re.findall("http://(.*)$",url)[0]
    reqPath = re.findall("/(.*)$", reqPath)[0]
    arg = {}

    path = "tab1/style_labels.html"
    arg["path"] = reqPath.split("/")
    return render_template(path,arg=arg)


##########################################
#   【视图类型】访问tab1中的tables标签页面
##########################################
@style.route('/tables')
def getTablesPage():
    #获取请求的路劲
    url = request.url
    reqPath = re.findall("http://(.*)$",url)[0]
    reqPath = re.findall("/(.*)$", reqPath)[0]
    arg = {}

    path = "tab1/style_tables.html"
    arg["path"] = reqPath.split("/")
    return render_template(path,arg=arg)

