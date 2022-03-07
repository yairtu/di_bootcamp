import flask

app = flask.Flask(__name__)

users = ["bob", "alice"]
# title, content, author
articles = [
	{
		"title": "article1",
		"content": "haslkdjfhad",
		"author": "bob"
	},
	{
		"title": "article2",
		"content": "haslkdjfhad",
		"author": "alice"
	}
]


@app.route('/blog')
def welcome_users():
	my_template = None
	with open('homepage.html', 'r') as f:
		my_template = f.read()

	return flask.render_template_string(my_template, users=users)


@app.route('/blog/articles')
def show_articles():
	my_template = None
	with open('articles.html') as f:
		my_template = f.read()
	return flask.render_template_string(my_template, articles=articles)


@app.route('/profile')
def profile():
	return flask.redirect(flask.url_for("welcome_users"))


if __name__ == "__main__":
	app.run(debug=True, port=5000)
