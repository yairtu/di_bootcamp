from flask import Flask, render_template
from get_requests import get_all_pokemon_names, get_pokemon_by_id, all_pokemon_types, all_pokemon_by_type

app = Flask(__name__)


@app.route('/')
def index():
	types = all_pokemon_types()
	return render_template('index.html', types=types)


@app.route('/pokemon/<pokemon_id>')
def show_pokemon_by_id(pokemon_id):
	pokemon = get_pokemon_by_id(pokemon_id)
	print(pokemon)
	return render_template("pokemon_details.html", pokemon=pokemon)


@app.route('/pokemons/bytype/<pokemon_type>')
def bytype(pokemon_type):
	pokemon_by_type = all_pokemon_by_type(pokemon_type)
	return render_template("bytype.html", pokemons=pokemon_by_type)


if __name__ == '__main__':
	app.run(host='localhost', port=8001, debug=True)
