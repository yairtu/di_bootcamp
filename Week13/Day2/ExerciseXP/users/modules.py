from users import db


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(32))
	street = db.Column(db.String(32))
	city = db.Column(db.String(32))
	zipcode = db.Column(db.String(32))

	def __repr__(self):
		return f"""
		ID: {self.id}
		Name: {self.name}
		Street: {self.street}
		City: {self.city}
		Zipcode: {self.zipcode}\n
		"""

# 	{
	# 		'id': self.id,
	# 		'name': self.name,
	# 		'street': self.street,
	# 		'city': self.street,
	# 		'zipcode': self.zipcode
	# 	}
