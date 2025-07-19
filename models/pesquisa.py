from database import db

class Pesquisa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(80), nullable=False)
    cidade = db.Column(db.String(80), nullable=False)
    bairro = db.Column(db.String(80), nullable=False)
    amostragem = db.Column(db.Integer, nullable=False)
    questionario = db.Column(db.JSON, nullable=False)
    prazo = db.Column(db.String(80), nullable=False)
    entrevistadores_atribuidos = db.Column(db.JSON, nullable=False)

    def __repr__(self):
        return f'<Pesquisa {self.titulo}>'
