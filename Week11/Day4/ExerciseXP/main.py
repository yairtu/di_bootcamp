from flask import Flask, url_for, render_template
import json

app = Flask(__name__)


def load_data():
	data = []
	with open('./static/product_db.json', 'r') as f:
		data = json.load(f)
	return data


@app.route('/')
@app.route('/#')
def homepage():
	css = open('./static/style.css').read()
	return render_template('homepage.html', css=css)


@app.route('/products.html')
def products():
	data = load_data()
	return render_template('products.html', products=data)


@app.route('/products/<product_id>')
def product_info(product_id):
	pass


if __name__ == '__main__':
	app.run(debug=True, port=5001)