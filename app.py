import os
from flaskr import create_app

if __name__ == "__main__":
    app = create_app()
    app.run(host=os.environ["FLASK_HOST"], port=os.environ["FLASK_PORT"])
