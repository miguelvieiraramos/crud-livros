from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class RegistrarAutor(FlaskForm):
    nome_autor = StringField('Nome do autor', validators=[DataRequired()])
    registrar = SubmitField('Registrar')
