from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('Index.html')

@app.route('/Spencer')
def Spencer():
    return render_template('SpencerPage.html')
@app.route('/Hiroki')
def Hiroki():
    return render_template('HirokiPage.html')
@app.route('/Charlie')
def Charlie():
    return render_template('CharliePage.html')
