from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired



class RegistrarLivro(FlaskForm):
    nome_livro = StringField('Nome do livro', validators=[DataRequired()])
    id_autor = SelectField('Nome do autor', coerce=int)
    registrar = SubmitField('Registrar')
