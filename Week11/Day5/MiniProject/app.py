from products_data import load_data, retrieve_requested_product
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


cart_item = []


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/products')
def products():
	data = load_data()
	return render_template('products.html', products=data)


@app.route('/products/<product_id>')
def product_info(product_id):
	item = retrieve_requested_product(product_id)
	return render_template('product_info.html', img=item['ProductPicUrl'], product=item)


@app.route('/cart')
def cart():
	total_price = 0
	global cart_item
	for item in cart_item:
		total_price += item['Price']
	return render_template('cart.html', total_price=total_price, products=cart_item)


@app.route('/add_product_to_cart/<product_id>')
def add_product_to_cart(product_id):
	product = retrieve_requested_product(product_id)
	global cart_item
	cart_item.append(product)
	return redirect(request.referrer)


@app.route('/delete_product_from_cart/<product_id>')
def delete_product_from_cart(product_id):
	product = retrieve_requested_product(product_id)
	global cart_item
	cart_item.remove(product)
	return redirect(request.referrer)


if __name__ == '__main__':
	app.run(host='localhost', port=8000, debug=True)