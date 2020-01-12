from flask import render_template, Blueprint, flash, redirect, url_for
from crud_livros.modelos import Livro, Autor
from crud_livros.livros.formularios import RegistrarLivro
from crud_livros import db
from crud_livros.autores.utils import capturar_autores

livros = Blueprint('livros', __name__)


@livros.route('/livros')
def home():
    livros_capturados = Livro.capturar_livro_autor()
    return render_template('livros.html', titulo="Livros", livros=livros_capturados)


@livros.route('/livros/adicionar', methods=['GET', 'POST'])
def adicionar_livro():
    formulario = RegistrarLivro()
    formulario.id_autor.choices = capturar_autores()
    if formulario.validate_on_submit():
        livro = Livro(formulario.nome_livro.data, formulario.id_autor.data)
        db.session.add(livro)
        db.session.commit()
        flash('Livro inserido com sucesso!', category='alert alert-success mt-2')
        return redirect(url_for('livros.home'))
    return render_template('adicionar_livro.html', formulario=formulario)


@livros.route('/livros/editar/<int:id_livro>', methods=['GET', 'POST'])
def editar_livro(id_livro):
    formulario = RegistrarLivro()
    livro = Livro.query.get_or_404(id_livro)
    formulario.id_autor.choices = capturar_autores()
    formulario.id_autor.default = livro.id_autor
    if formulario.validate_on_submit():
        livro.nome = formulario.nome_livro.data
        livro.id_autor = formulario.id_autor.data
        db.session.commit()
        flash('Livro editado com sucesso!', category='alert alert-primary mt-2')
        return redirect(url_for('livros.home'))
    formulario.process()
    return render_template('editar_livro.html', formulario=formulario, livro=livro)


@livros.route('/livros/excluir/<int:id_livro>', methods=['GET', 'POST'])
def excluir_livro(id_livro):
    livro = Livro.query.get_or_404(id_livro)
    db.session.delete(livro)
    db.session.commit()
    flash('Livro editado com sucesso!', category='alert alert-danger mt-2')
    return redirect(url_for('livros.home'))

