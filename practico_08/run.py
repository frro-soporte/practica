from autogestion_alumnos import db, create_app
from autogestion_alumnos.config import Config

app = create_app(Config)

if __name__ == '__main__':
    db.create_all()
    app.run(port=3002, debug=True)
