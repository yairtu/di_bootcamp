from app import db


class Todo(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
	details = db.Column(db.String(30), index=True)
	completed = db.Column(db.Boolean, default=False)

	def save_task_to_db(self):
		db.session.add(self)
		db.session.commit()

	def set_task_as_completed(self):
		self.completed = True
		db.session.commit()

	def set_task_as_uncompleted(self):
		self.completed = False
		db.session.commit()

	def delete_from_todo(self):
		db.session.delete(self)
		db.session.commit()
