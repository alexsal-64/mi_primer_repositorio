from flask import Flask
from models import db
from admin import admin_bp
from user import user_bp
import os

app = Flask(__name__)

# Configuración robusta para la base de datos usando ruta absoluta
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'instance', 'peliculas.db')
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "ve10x172859n"

db.init_app(app)

app.register_blueprint(admin_bp)
app.register_blueprint(user_bp)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)