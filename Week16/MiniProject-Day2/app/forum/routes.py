import requests
from flask import Blueprint, render_template, redirect, url_for, abort, flash, request
from flask_login import current_user, login_required
from sqlalchemy import desc

from app import db
from app.forum.forms import PostForm, CommentForm
from app.models import Card, Post, Comment

forum = Blueprint('forum', __name__)


@forum.route('/forum', methods=['GET', 'POST'])
@login_required
def forum_home():
	page = request.args.get('page', 1, type=int)
	posts = Post.query.order_by(desc(Post.date_posted)).paginate(per_page=5)
	comments = Comment.query.all()
	form = PostForm()
	cards = current_user.card
	if form.validate_on_submit():
		try:
			new_post = Post(title=form.title.data, content=form.content.data, user=current_user,
							card=form.card.data.image_url, price=form.card.data.price)
			db.session.add(new_post)
			db.session.commit()
		except AttributeError:
			new_post = Post(title=form.title.data, content=form.content.data, user=current_user,
							card=None, price=None)
			db.session.add(new_post)
			db.session.commit()
		return redirect(url_for('forum.forum_home'))
	return render_template('forum/forum.html', posts=posts, form=form, cards=cards, comments=comments)


@forum.route('/forum/post')
def post():
	return


@forum.route('/forum/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete(id):
	post = Post.query.get_or_404(id)
	if current_user != post.user:
		abort(403)
	else:
		post.delete_post()
	return redirect(url_for('forum.forum_home'))


@forum.route('/forum/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
	form = PostForm()
	cform = CommentForm()
	post = Post.query.get_or_404(id)
	if current_user != post.user:
		abort(403)
	if form.validate_on_submit():
		post.title = form.title.data
		post.content = form.content.data
		post.price = form.card.data.price
		post.card = form.card.data.image_url
		db.session.commit()
		flash('Post updated successfully', 'success')
		return redirect(url_for('forum.forum_home'))
	return render_template('forum/edit.html', form=form, cform=cform)


@forum.route('/forum/buy/<id>', methods=['GET', 'POST'])
@login_required
def buy(id):
	post = Post.query.filter_by(id=id).first()
	if not post.sold:
		card = Card.query.filter_by(image_url=post.card).first()
		if card.rarity == 'Common':
			current_user.points += 1
		elif card.rarity == 'Rare':
			current_user.points += 2
		elif card.rarity == 'Super Rare':
			current_user.points += 3
		elif card.rarity == 'Ultra Rare':
			current_user.points += 4
		else:
			current_user.points += 5
		post.user.card.remove(card)
		post.user.credits += float(card.price)
		current_user.credits -= float(card.price)
		current_user.card.append(card)
		post.sold = True
		db.session.commit()
		flash(f"Congratulations! You just bought {card.name} for ${card.price}", 'success')
	else:
		abort(403)
	return redirect(url_for('forum.forum_home'))


@forum.route('/forum/comment/<int:id>', methods=['POST', 'GET'])
@login_required
def comment(id):
	post = Post.query.filter_by(id=id).first()
	form = CommentForm()
	if form.validate_on_submit():
		comment = Comment(content=form.content.data, user=current_user, post=post)
		db.session.add(comment)
		db.session.commit()
		return redirect(url_for('forum.forum_home'))
	return render_template('forum/comment.html', form=form)
