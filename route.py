
from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from models import User, Contact
from web.__init__ import db
from flask_login import login_user, logout_user, login_required, current_user

routes = Blueprint('routes', __name__)

@routes.route('/home')
@login_required
def home():
    return render_template("home.html", user=current_user)

@routes.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('routes.home'))

@routes.route('/', methods=['GET', 'POST'])
def authentified():

    if request.method == 'POST':

    
        action = request.form.get('action')

        nom = request.form.get('nom')
        email = request.form.get('email')
        mdp = request.form.get('mdp')

        
        if action == 'signup':

            user = User.query.filter_by(email=email).first()

            if user:
                flash('Cet utilisateur existe déjà', category='warning')

            elif not nom or not email or not mdp:
                flash('Tous les champs sont obligatoires', category='error')

            else:

                new_user = User(
                    nom=nom,
                    email=email,
                    mdp=generate_password_hash(
                        mdp,
                        method="pbkdf2:sha256"
                    )
                )

                db.session.add(new_user)
                db.session.commit()
                login_user(new_user, remember=True)
                return redirect(url_for('routes.home'))

       
        elif action == 'login':

            user = User.query.filter_by(nom=nom).first()

            if user:

                if check_password_hash(user.mdp, mdp):
                    # connexion reussie
                    login_user(user, remember=True)
                    return redirect(url_for('routes.home'))
                    

                else:
                    flash(
                        'Mot de passe incorrect, ressayer',
                        category='error'
                    )

            else:
                flash(
                    'Cet utilisateur n\'existe pas',
                    category='error'
                )
                return render_template ('signup.html')

    return render_template("signup.html")
