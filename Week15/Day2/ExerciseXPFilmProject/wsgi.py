from app import create_app, db


if __name__ == "__main__":  # Protect this code to be ran if he is imported
	flask_app = create_app()
	db.create_all(app=flask_app)

	flask_app.run(port=5511, debug=True)