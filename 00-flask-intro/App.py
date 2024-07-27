from flask import Flask, render_template
import jinja2
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('hello.html', person= 'shivansh')

@app.route('/h')
def bye():
    return 'Bye, World!'


if __name__ == '__main__':
    app.run(debug=True)
