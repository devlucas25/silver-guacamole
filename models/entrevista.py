from database import db

class Entrevista(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pesquisa_id = db.Column(db.Integer, db.ForeignKey('pesquisa.id'), nullable=False)
    entrevistador_id = db.Column(db.Integer, db.ForeignKey('entrevistador.id'), nullable=False)
    respostas = db.Column(db.JSON, nullable=False)
    localizacao = db.Column(db.String(80), nullable=False)
    observacoes = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f'<Entrevista {self.id}>'
