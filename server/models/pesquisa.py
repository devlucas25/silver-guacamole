from datetime import datetime

class Pesquisa:
    def __init__(self, titulo, cidade, bairro, amostragem, questionario, prazo, entrevistadores_atribuidos):
        self.titulo = titulo
        self.cidade = cidade
        self.bairro = bairro
        self.amostragem = amostragem
        self.questionario = questionario
        self.prazo = prazo
        self.entrevistadores_atribuidos = entrevistadores_atribuidos
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
