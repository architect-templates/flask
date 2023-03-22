import os
from flask import Flask
from controller import controller_bp
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("POSTGRES_URL")
app.register_blueprint(controller_bp)

db.init_app(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    
    app.run(debug=True)
