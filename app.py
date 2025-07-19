from flask import Flask, jsonify, request
from database import db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pesquisas.db'
    db.init_app(app)

    from models.pesquisa import Pesquisa
    from models.entrevistador import Entrevistador
    from models.administrador import Administrador
    from models.entrevista import Entrevista

    @app.cli.command("create-db")
    def create_db_command():
        with app.app_context():
            db.create_all()
        print("Banco de dados criado.")

    @app.route("/pesquisas", methods=["POST"])
    def criar_pesquisa():
        dados = request.get_json()
        pesquisa = Pesquisa(
            titulo=dados["titulo"],
            cidade=dados["cidade"],
            bairro=dados["bairro"],
            amostragem=dados["amostragem"],
            questionario=dados["questionario"],
            prazo=dados["prazo"],
            entrevistadores_atribuidos=dados["entrevistadores_atribuidos"],
        )
        db.session.add(pesquisa)
        db.session.commit()
        return jsonify(pesquisa.id)

    @app.route("/pesquisas", methods=["GET"])
    def listar_pesquisas():
        pesquisas = Pesquisa.query.all()
        return jsonify([p.titulo for p in pesquisas])

    @app.route("/auth/entrevistador/register", methods=["POST"])
    def registrar_entrevistador():
        dados = request.get_json()
        entrevistador = Entrevistador(
            nome=dados["nome"],
            email=dados["email"],
            senha=dados["senha"],
        )
        db.session.add(entrevistador)
        db.session.commit()
        return jsonify(entrevistador.id)

    @app.route("/auth/admin/register", methods=["POST"])
    def registrar_admin():
        dados = request.get_json()
        admin = Administrador(
            nome=dados["nome"],
            email=dados["email"],
            senha=dados["senha"],
        )
        db.session.add(admin)
        db.session.commit()
        return jsonify(admin.id)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
