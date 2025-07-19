from datetime import datetime

class Entrevista:
    def __init__(self, pesquisa_id, entrevistador_id, respostas, localizacao, observacoes=None):
        self.pesquisa_id = pesquisa_id
        self.entrevistador_id = entrevistador_id
        self.respostas = respostas
        self.localizacao = localizacao
        self.observacoes = observacoes
        self.created_at = datetime.now()
