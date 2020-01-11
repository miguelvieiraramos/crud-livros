from crud_livros.modelos import Autor

def capturar_autores():
    autores = Autor.query.all()
    autores_organizados = []
    for autor in autores:
        autores_organizados.append((autor.id, autor.nome))
    return autores_organizados