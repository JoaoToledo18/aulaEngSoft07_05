from repositories.sessao_repository import SessaoRepository

class SessaoService:

    def __init__(self):
        self.repository = SessaoRepository()

    def cadastrar_sessao(self, sessao):

        if not sessao.data:
            raise Exception("Data inválida")

        if not sessao.horario:
            raise Exception("Horário inválido")

        self.repository.salvar(sessao)