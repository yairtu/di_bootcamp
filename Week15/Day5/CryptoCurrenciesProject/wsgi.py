from webapp import create_app, db

if __name__ == '__main__':
	app = create_app()
	db.create_all(app=app)
	app.run(port=5222, debug=True)
