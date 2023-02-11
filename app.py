from flask import Flask, render_template, request, flash
from flask_wtf import CSRFProtect
from flask_migrate import Migrate

from forms import SignupForm
from config import Config
from models import db, User


app = Flask(__name__)
app.config.from_object(Config)

csrf = CSRFProtect(app)
migrate = Migrate()

db.init_app(app)
csrf.init_app(app)
migrate.init_app(app, db)


@app.route("/")
def inicio():
    return render_template('index.html')


@app.route("/signup", methods=['GET','POST'])
def signup():
    form = SignupForm()
    
    if request.method == 'POST' and form.validate_on_submit():
        username=form.username.data
        full_name=form.full_name.data
        DNI = form.DNI.data
        nombre = form.nombre.data
        raza = form.raza.data
        fecha = form.fecha.data
        existing_user= User.query.filter_by(username=username).first()
        if not existing_user:
            user = User(
                username=username,
                full_name=full_name,
                DNI=DNI,
                nombre=nombre,
                raza=raza,
                fecha=fecha
            )
           
            db.session.add(user)
            db.session.commit()
            flash("Usuario registrado")
        else:
            flash("El usuario ya existe")
         
    return render_template('registrarse.html', form=form)
    
    
@app.route("/actualizar")
def actualizar():
    return render_template('actualizar.html')

