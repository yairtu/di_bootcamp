from flask import Blueprint, render_template

from app import db
from app.films.forms import AddDirectorForm, AddFilmForm
from app.models import Film, Director

films = Blueprint('film', __name__, url_prefix='/films', template_folder='templates', static_folder='static', )


@films.route('/homepage')
def home():
	# new_film = Film(title="Aquaman", category="Action")
	# db.session.add(new_film)
	# db.session.commit()
	all_films = Film.query.all()
	return render_template('homepage.html', films=all_films)


@films.route('/addDirector', methods=['GET', 'POST'])
def add_director():
	form = AddDirectorForm()
	if form.validate_on_submit():
		director = Director(first_name=form.first_name.data, last_name=form.last_name.data)
		db.session.add(director)
		db.session.commit()
	return render_template('director/addDirector.html', form=form)


@films.route('/addFilm')
def add_film():
	form = AddFilmForm()

	return render_template('film/addFilm.html', form=form)
