from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField
from wtforms.validators import DataRequired, Length

class SignupForm(FlaskForm):
    username = StringField("Username de la mascota", validators=[DataRequired()])
    nombre = StringField("Nombre de la mascota", validators=[DataRequired()])
    raza = StringField("Raza", validators=[DataRequired()])
    fecha = DateField("Fecha de nacimiento de la Mascota")
    full_name = StringField("Nombre Completo del propietario", validators=[DataRequired()])
    DNI =StringField("DNI", validators=[DataRequired(), Length(min=8, max=8,message="El DNI tiene 8 digitos")])
    submit = SubmitField('Registrarse')
