from services.sessao_service import SessaoService
from models.sessao import Sessao

class SessaoController:

    def __init__(self):
        self.service = SessaoService()

    def cadastrar(self, filme_id, cinema_id, data, horario):

        sessao = Sessao(
            id=None,
            filme_id=filme_id,
            cinema_id=cinema_id,
            data=data,
            horario=horario,
            publico=0
        )

        self.service.cadastrar_sessao(sessao)