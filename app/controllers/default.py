from flask import render_template, flash
from flask_login import login_user
from app import app, db

from app.modells.tables import User
from app.modells.forms import LoginForm


@app.route("/index")
@app.route("/")
def index():
    return render_templates('index.html')


@app.route("/login", methods=[" GET", "POST"]).first()
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.data.password:
            login_user(user)
            flash("Logged in.")
        else:
            flash("Invalid login.")

    return render_templates('login.html', form=form)

@app.route("/teste/<info>")
@app.route("/teste", defaults={"info": None})
def teste():
    i = User("Maria","1234","Maria Jose", "Maria@Gmail.com")
    db.session.add(i)
    db.session.commit()

