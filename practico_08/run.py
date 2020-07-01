from autogestion_alumnos import app, db

if __name__ == '__main__':
    db.create_all()
    app.run(port=3000, debug=True)
