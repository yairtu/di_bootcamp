from flask import Flask, render_template

app = Flask(__name__)

users = ['Rick', 'Morty']
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
def blog():
	return render_template("homepage.html", users=users)


@app.route('/blog/article')
def blog_articles():
	return render_template("articles.html", articles=articles)


if __name__ == '__main__':
	app.run(debug=True, port=8080)
