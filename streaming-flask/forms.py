from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length

class AdminLoginForm(FlaskForm):
    username = StringField("Usuario", validators=[DataRequired(), Length(max=80)])
    password = PasswordField("Contraseña", validators=[DataRequired()])
    submit = SubmitField("Ingresar")

class PeliculaForm(FlaskForm):
    titulo = StringField("Título", validators=[DataRequired(), Length(max=100)])
    descripcion = StringField("Descripción", validators=[Length(max=300)])
    anio = IntegerField("Año")
    submit = SubmitField("Agregar Película")