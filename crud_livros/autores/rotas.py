from flask import Blueprint, render_template, request, flash, redirect, url_for
from crud_livros.autores.formularios import RegistrarAutor
from crud_livros.modelos import Autor
from crud_livros import db

autores = Blueprint('autores', __name__)


@autores.route('/autores')
def home():
    autores_capturados = Autor.query.all()
    return render_template('autores.html', path=request.path, autores=autores_capturados, titulo="Autores")


@autores.route('/autores/adicionar', methods=['GET', 'POST'])
def adicionar_autor():
    formulario = RegistrarAutor()
    if formulario.validate_on_submit():
        autor = Autor(nome=formulario.nome_autor.data)
        db.session.add(autor)
        db.session.commit()
        flash('Autor inserido com sucesso!', 'alert alert-success mt-2')
        return redirect(url_for('autores.home'))
    return render_template('adicionar_autor.html', path=request.path[:8], formulario=formulario, titulo="Adicionar autor")


@autores.route('/autores/editar/<int:id_autor>', methods=['GET', 'POST'])
def editar_autor(id_autor):
    formulario = RegistrarAutor()
    autor = Autor.query.get_or_404(id_autor)
    if formulario.validate_on_submit():
        autor.nome = formulario.nome_autor.data
        db.session.commit()
        flash('Autor editado com sucesso!', 'alert alert-primary mt-2')
        return redirect(url_for('autores.home'))
    return render_template('editar_autor.html', path=request.path[:8], formulario=formulario, autor=autor, titulo="Editar autor")


@autores.route('/autores/excluir/<int:id_autor>', methods=['GET', 'POST'])
def excluir_autor(id_autor):
    autor = Autor.query.get_or_404(id_autor)
    db.session.delete(autor)
    db.session.commit()
    flash('Autor excluido com sucesso!', 'alert alert-danger mt-2')
    return redirect(url_for('autores.home'))
