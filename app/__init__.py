from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # --- ajuste a URI abaixo para seu MySQL (ou use sqlite para testes) ---
    # exemplo MySQL: 'mysql+pymysql://usuario:senha@localhost/nome_do_banco'
    # para teste rápido local sem MySQL, pode usar sqlite:
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///estoque.db'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///estoque.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    # importa rotas (depois de criar o app)
    from app import routes
    app.register_blueprint(routes.bp)

    return app
