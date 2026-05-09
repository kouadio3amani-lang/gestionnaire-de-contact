from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import check_password_hash, generate_password_hash
routes =Blueprint('routes', __name__)
@routes.route('/')
def home():
    return render_template("home.html")
@routes.route('/signup', methods = ["GET", "POST"])
def sign_up():
    return render_template("signup.html")
@routes.route('/login')
def login():
    return render_template("login.html")