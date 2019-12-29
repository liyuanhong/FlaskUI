from flask import Flask, redirect

from views.tab1.style import style
from views.tab1.icon import icon
from views.tab2.login import login
from views.tab2.example import example
from views.other import other

app = Flask(__name__)
app.register_blueprint(style,url_prefix = "/tab1/style")
app.register_blueprint(icon,url_prefix = "/tab1/icon")
app.register_blueprint(login,url_prefix = "/tab2/login")
app.register_blueprint(example,url_prefix = "/tab2/example")
app.register_blueprint(other,url_prefix = "/other")

@app.route('/')
def hello():
    return redirect('/tab1/style')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')