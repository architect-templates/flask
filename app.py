import os
from flaskr import create_app
from livereload import Server

if __name__ == "__main__":
    app = create_app()
    # app.debug = True

    # server = Server(app.wsgi_app)
    # def alert():
    #   print('--> here')
    # server.watch('flaskr/templates/blog/index.html', alert)
    # server.serve(host="0.0.0.0", port=os.environ["FLASK_PORT"])

    app.run(host="0.0.0.0", port=os.environ["FLASK_PORT"], use_reloader=True)
