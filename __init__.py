'''
from flask import Flask
from views.robots import robots
from views.test import test

app = Flask(__name__)
app.register_blueprint(robots)
app.register_blueprint(test)

@app.route('/')
def index():
    return '<h1>index</h1>'

if __name__ == '__main__':
    app.run(debug=True)
'''