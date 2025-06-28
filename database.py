from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def init_db(app):
  app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:MSsbRqbNKmEWrvEVNbaLmeTZmyDNAkMz@centerbeam.proxy.rlwy.net:18566/mindmate'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

  db.init_app(app)
