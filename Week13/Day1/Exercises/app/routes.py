from flask import flash, render_template
from app import app


@app.route('/')
def index():
	flash("This is a flashed message")
	flash("Here is another flashed message")
	return render_template('index.html')