from datetime import datetime
from flask import Flask, render_template_string, render_template

# Exercise 1
app = Flask(__name__)

# current_time = datetime.now()


# @app.route('/')
# def index():
# 	# my_template = None
# 	# with open('./templates/index.html', 'r') as f:
# 	# 	my_template = f.read()
# 	# html = render_template('index.html', current_time=current_time)
# 	return str(datetime.now())

# Exercise 2
@app.route('/')
def index():
	current_time = datetime.now()
	if 8 <= current_time.hour < 13:
		return 'Good morning'
	elif 13 <= current_time.hour < 17:
		return 'Good afternoon'
	elif 17 <= current_time.hour < 21:
		return 'Good evening'
	else:
		return "Good night"


if __name__ == '__main__':
	app.run(debug=True, port=10001)
