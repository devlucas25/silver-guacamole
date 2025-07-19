from database import db

class Entrevistador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'<Entrevistador {self.nome}>'
