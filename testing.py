from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/service')
def good():
    return render_template('service.html')




# 6 => home,about ,service ,contact ,login ,register
