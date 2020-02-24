from crud_livros import db


class Autor(db.Model):
    __tablename__ = 'autor'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), unique=True, nullable=False)
    livros = db.relationship('Livro', backref='autor', cascade="all, delete")

    def __repr__(self):
        return f'{self.nome} {self.id}'

    def __init__(self, nome):
        self.nome = nome


class Livro(db.Model):
    __tablename__ = 'livro'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), unique=True, nullable=False)
    id_autor = db.Column(db.Integer, db.ForeignKey('autor.id'), nullable=False)

    @staticmethod
    def capturar_livro_autor():
        return db.session.query(Livro, Autor).join(Autor, Livro.id_autor == Autor.id).all()

    def __repr__(self):
        return f'{self.id} {self.nome}'

    def __init__(self, nome, id_autor):
        self.nome = nome
        self.id_autor = id_autor
