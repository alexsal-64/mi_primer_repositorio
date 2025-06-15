from flask import Blueprint, render_template, redirect, url_for, session, request, flash
from models import db, Pelicula, Admin
from forms import PeliculaForm, AdminLoginForm

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

def is_logged_in():
    return session.get("admin_logged_in", False)

@admin_bp.route("/login", methods=["GET", "POST"])
def login():
    form = AdminLoginForm()
    if form.validate_on_submit():
        admin = Admin.query.filter_by(username=form.username.data).first()
        if admin and admin.check_password(form.password.data):
            session["admin_logged_in"] = True
            return redirect(url_for("admin.admin_index"))
        flash("Usuario o contraseña incorrectos", "danger")
    return render_template("admin/login.html", form=form)

@admin_bp.route("/logout")
def logout():
    session.pop("admin_logged_in", None)
    flash("Sesión cerrada", "info")
    return redirect(url_for("admin.login"))

@admin_bp.route("/", methods=["GET", "POST"])
def admin_index():
    if not is_logged_in():
        return redirect(url_for("admin.login"))
    form = PeliculaForm()
    if form.validate_on_submit():
        nueva_pelicula = Pelicula(
            titulo=form.titulo.data,
            descripcion=form.descripcion.data,
            anio=form.anio.data
        )
        db.session.add(nueva_pelicula)
        db.session.commit()
        return redirect(url_for("admin.admin_index"))
    peliculas = Pelicula.query.all()
    return render_template("admin/admin_index.html", peliculas=peliculas, form=form)