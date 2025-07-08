from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)


@app.route('/roy')
def roy():
    return render_template('template.html',
                           name='Roy',
                           acronym='gtg')