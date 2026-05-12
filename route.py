# from flask import Blueprint, render_template, request, flash, redirect, url_for
# from werkzeug.security import check_password_hash, generate_password_hash
# from models import User, Contact
# from web.__init__ import db
# from flask_login import user_logged_in, login_user, logout_user, login_required
# routes =Blueprint('routes', __name__)
# @routes.route('/')
# @login_required
# def home():
#     return render_template("home.html")
# @routes.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('routes.login'))
# @routes.route('/signup', methods = ["GET", "POST"])
# def sign_up():
    
#     if request.method == 'POST':
#         nom = request.form.get('nom')
#         email = request.form.get('email')
#         mdp = request.form.get('mdp')
#         user = User.query.filter_by(email = email).first()
#         if user:
#             flash('Cet utilisateur existe déjà', category='warning')
#             return render_template('signup.html')
#         elif not email or not mdp:
#             flash('Tu es entrain de faire une betise', category='error')
#             return render_template('signup.html')
#         elif len(email) < 4:
#             flash("Le l'email doit dépasser 4 caractère", category='error')
#             return render_template('signup.html')
#         elif len(mdp) < 7:
#             flash('Le mot de passe doit dépasser 7 caractère', category='error')
#             return render_template('signup.html')
#         else:
#             flash("Compte créer avec succès", category='success')
#             new_user = User(nom = nom, email=email, mdp = generate_password_hash(mdp, method="pbkdf2:sha256"))
#             db.session.add(new_user)
#             db.session.commit()
#             return redirect(url_for('routes.home'))

    
#     return render_template('signup.html')
# @routes.route('/login', methods = ['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         nom = request.form.get('nom')
#         mdp = request.form.get('mdp')
#         user = User.query.filter_by(nom = nom).first()
#         if user:
#             if check_password_hash(user.mdp, mdp):
#                 flash('Connexion effectuée avec succès', category='success')
#                 return redirect(url_for('routes.home'))
#                 login_user(user, remember=True)
#             else:
#                 flash('Mot de passe incorrect, ressayer', category='error')
#         else:
#             flash('Restez concentré. Ce nom n\'existe pas', category='error')
#     return render_template("login.html")
from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from models import User, Contact
from web.__init__ import db
from flask_login import login_user, logout_user, login_required

routes = Blueprint('routes', __name__)

@routes.route('/')
@login_required
def home():
    return render_template("home.html")

@routes.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('routes.auth'))

@routes.route('/signup', methods=['GET', 'POST'])
def signup():

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

            elif len(email) < 4:
                flash("L'email doit dépasser 4 caractères", category='error')

            elif len(mdp) < 7:
                flash('Le mot de passe doit dépasser 7 caractères', category='error')

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

                flash("Compte créé avec succès", category='success')

                return redirect(url_for('routes.home'))

       
        elif action == 'login':

            user = User.query.filter_by(email=email).first()

            if user:

                if check_password_hash(user.mdp, mdp):

                   
                    login_user(user, remember=True)

                    flash(
                        'Connexion effectuée avec succès',
                        category='success'
                    )

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