from flask import Blueprint, render_template, request, jsonify
from models import db, Movie
from sqlalchemy.exc import IntegrityError

controller_bp = Blueprint('controller', __name__)

@controller_bp.route('/')
def home():
    items = Movie.query.all()
    return render_template('index.html', items=items)

@controller_bp.route('/api/items')
def get_movies():
    items = Movie.query.all()

    item_list = []
    for item in items:
        item_data = { 'name': item.title, 'rating': item.rating }
        item_list.append(item_data)

    return jsonify(item_list), 200

@controller_bp.route('/api/item', methods=['POST'])
def create_movie():
    data = request.get_json()
    new_movie = Movie(
        title=data['name'],
        rating=data['rating']
    )
    db.session.add(new_movie)

    try:
        db.session.commit()
        return jsonify({ 'message': 'Movie created successfully' }), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({ 'message': 'Movie already exists' }), 400
