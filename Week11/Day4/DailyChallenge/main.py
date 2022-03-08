from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
	return render_template("index.html")


@app.route('/blue.html')
def blue():
	return render_template("color.html")


@app.route('/red.html')
def red():
	return render_template("color.html")


@app.route('/green.html')
def green():
	return render_template("color.html")


@app.route('/yellow.html')
def yellow():
	return render_template("color.html")


app.run(debug=True, port=5002)
