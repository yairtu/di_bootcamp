from app import flask_app
from flask import render_template, redirect, url_for
from app.forms import AddTodo, MarkCompleted
from app import db
from app.models import Todo


@flask_app.route('/', methods=['GET', 'POST'])
def index():
	form = AddTodo()
	completed = MarkCompleted()
	all_tasks = Todo.query.all()
	if form.validate_on_submit():
		task = form.todo.data
		new_task = Todo(details=task)
		new_task.save_task_to_db()
		return redirect(url_for('index'))
	return render_template('index.html', completed=completed, form=form, all_tasks=all_tasks)


@flask_app.route('/complete/<int:todo_id>', methods=['GET'])
def mark_completed(todo_id):
	todo_item = Todo.query.get(todo_id)
	todo_item.set_task_as_completed()
	return redirect(url_for('index'))


@flask_app.route('/uncompleted/<int:todo_id>', methods=['GET'])
def mark_uncompleted(todo_id):
	todo_item = Todo.query.get(todo_id)
	todo_item.set_task_as_uncompleted()
	return redirect(url_for('index'))


@flask_app.route('/delete/<int:todo_id>', methods=['GET'])
def delete(todo_id):
	todo_item = Todo.query.get(todo_id)
	todo_item.delete_from_todo()
	return redirect(url_for('index'))


@flask_app.route('/clear_all')
def clear():
	Todo.query.delete()
	db.session.commit()
	return redirect(url_for('index'))
