from flask import render_template, url_for, flash, redirect,session
from gecole import app, db
from gecole.forms import LoginForm, AjouterEleve, AjouterClasse
from gecole.models import User, Classes, Eleves


@app.route("/")
def home():
    return render_template('pages/home.html')

@app.route("/accueil")
def accueil():
    clses = Classes.query.all()
    return render_template('pages/accueil.html',clses = clses)

@app.route("/eleve", methods=['GET','POST'])
def eleve():
    form = AjouterEleve()
    if form.validate_on_submit():
        el = Eleves(prenom = form.prenom.data,nom=form.nom.data,classe=form.classe.data)
        db.session.add(el)
        db.session.commit()
        flash('L eleve a été bien enregistrer ','success')
        return redirect(url_for('listeEleves'))
    return render_template('pages/ajoutEleve.html', title = 'Ajouter Eleve', form = form)

@app.route("/classe", methods=['GET','POST'])
def classe():
    form = AjouterClasse()
    if form.validate_on_submit():
        cl = Classes(nom_classe = form.nom_classe.data)
        db.session.add(cl)
        db.session.commit()
        flash('Le classe a été bien créer','success')
        return redirect(url_for('listeClasses'))
    else:
        flash('La classe existe deja dans notre base de donnée')
    return render_template('pages/AjoutClasse.html', title = 'Ajouter Classe', form = form)

@app.route("/listeEleves")
def listeEleves():
    eleves = Eleves.query.all()
    return render_template('pages/eleve.html', title = 'Liste Eleve',eleves = eleves)

@app.route("/listeClasses")
def listeClasses():
    classes = Classes.query.all()
    return render_template('pages/classe.html', title = 'Liste Classe', classes = classes)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@gecole.com' and form.password.data == 'admin':
            session['conn'] = True
            flash('Vous etes connecté avec success!', 'success')
            return redirect(url_for('accueil'))
        else:
            flash('Email ou mot de passe incorect.', 'danger')
    return render_template('pages/login.html', title='Connexion', form=form)
 

@app.route("/logout")
def logout():
    session['conn'] = False
    return home()
