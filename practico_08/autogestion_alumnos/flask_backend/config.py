class Config:
    SECRET_KEY = 'frro_soporte'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///autogestionalumnos.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'frro_soporte_jwt'
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access']
