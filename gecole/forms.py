from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField, SelectField
from wtforms.validators import DataRequired, Email,Length


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Connexion')

class AjouterEleve(FlaskForm):
    prenom = StringField('Prenom',
                           validators=[DataRequired(), Length(min=2, max=60)])
    nom = StringField('Nom',
                           validators=[DataRequired(), Length(min=2, max=60 )])              
    classe = SelectField('Classe',validators=[DataRequired()],
        choices=[('Terminal', 'Terminal'), ('Premiere', 'Premiere'), ('Seconde', 'Seconde')]
    )
    submit = SubmitField('Ajouter éléve')

class AjouterClasse(FlaskForm):
    nom_classe = StringField('Intitulé de la classe',
                           validators=[DataRequired(), Length(min=2, max=60)])
    submit = SubmitField('Ajouter classe')