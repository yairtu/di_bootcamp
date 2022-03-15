from flask import Flask, render_template, flash, redirect, url_for, request
from forms import CvDetails
import json
from json_data import load_data

app = Flask(__name__)

app.config['SECRET_KEY'] = 'dbdbc16257d93500'


@app.route('/', methods=["GET", "POST"])
def index():
	form = CvDetails()
	if form.validate_on_submit():
		file = "./static/form_data.json"
		with open(file, 'w') as f:
			json.dump(form.data, f, indent=4)
		flash(f"CV Created for {form.first_name.data} {form.last_name.data}!", "success")
		return redirect(url_for('cv'))
	return render_template('index.html', title='Form for cv', form=form)


@app.route('/cv', methods=["GET", "POST"])
def cv():
	form_data = load_data()
	return render_template('cv.html', title='My CV', form=form_data)


if __name__ == '__main__':
	app.run(host='localhost', port=8001, debug=True)
