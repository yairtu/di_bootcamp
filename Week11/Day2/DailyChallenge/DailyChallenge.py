from flask import Flask, render_template
from markdown import markdown

app = Flask(__name__)


@app.route('/exercises')
def exercises():
	with open("./lesson1/exercises.md", "r") as f:
		text = f.read()
		html = markdown(text)
		return html


@app.route('/lesson')
def lesson():
	with open("./lesson1/in-this-chapter.md", "r") as f:
		text = f.read()
		html = markdown(text)
		return html


if __name__ == '__main__':
	app.run(debug=True, port=5000)
