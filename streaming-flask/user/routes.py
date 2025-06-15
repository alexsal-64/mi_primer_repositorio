from flask import Blueprint, render_template
from models import Pelicula

user_bp = Blueprint("user", __name__)

@user_bp.route("/")
def user_index():
    peliculas = Pelicula.query.all()
    return render_template("user/user_index.html", peliculas=peliculas)