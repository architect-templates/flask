from flask import Flask
from flask import request
import os
from time import sleep
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.sql import text

from flask import jsonify

"""Wait until database is initialized to start app""" 
# Build connection string
db_addr = os.environ.get('DB_ADDR').split('//')
db_creds = os.environ.get('DB_USER') + ':' + os.environ.get('DB_PASS')
db_connection_string = db_addr[0] + '//' + db_creds + '@' + db_addr[1]

database_is_down = True
while database_is_down:
    try:
        # Keep trying connections until database is ready
        engine = create_engine(db_connection_string)
        with engine.connect() as connection:
            connection.execute(text("select 1"))
            database_is_down = False
    except:
        sleep(2)


"""Start app build"""
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_connection_string
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

## Define our database
class Item(db.Model):
    __tablename__ = 'Item'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    rating = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return str({"name": self.name, "rating":self.rating})

db.create_all()

@app.route("/", methods=['GET', 'POST'])
@app.route("/movies", methods=['GET', 'POST'])
@app.route("/items", methods=['GET', 'POST'])
def index():
    """Create new movie entry"""
    if request.method == "POST":
        data = request.get_json()
        name = data['name']
        rating = data['rating']
        error = None

        if not name:
            error = "Movie title is required."
        elif not rating:
            error = "Rating is required."
        elif rating > 5 or rating < 1:
            error = "Choose rating between 1-5"

        if error is not None:
            return {'error': error}
        else:
            # Write to database
            entry = Item(name=name, rating=rating)
            db.session.add(entry)
            db.session.commit()

    """Grab all movies in db"""
    output = ''
    try:
        output = Item.query.all()
        output = jsonify(eval(repr(output)))
    except Exception as e:
        header = '<h1>Something is broken.</h1>'
        error_text = "<p>Error:<br>" + str(e) + "</p>"
        return {'error': header + error_text}

    return output