import getpass
from datetime import date

from app.core.database import Database
from app.core.senha_utils import Senha_Utils

from app.dao.estado_dao import Estado_DAO
from app.dao.cidade_dao import Cidade_DAO
from app.dao.perfil_dao import Perfil_DAO
from app.dao.usuario_dao import Usuario_DAO

from app.models.estado import Estado
from app.models.cidade import Cidade
from app.models.perfil import Perfil
from app.models.usuario import Usuario


def obter_ou_criar_estado(estado_dao):
    estados = estado_dao.get_all()
    if estados:
        return estados[0]
    return estado_dao.save(Estado(None, "Não informado", "XX"))


def obter_ou_criar_cidade(cidade_dao, estado):
    cidades = cidade_dao.get_all()
    if cidades:
        return cidades[0]
    return cidade_dao.save(Cidade(None, "Não informada", estado))


def obter_ou_criar_perfil_administrador(perfil_dao):
    for perfil in perfil_dao.get_all():
        if perfil.nome == "ADMINISTRADOR":
            return perfil
    return perfil_dao.save(
        Perfil(
            None,
            "Administrador",
            "Perfil inicial com acesso administrativo, criado pelo seed."
        )
    )


def criar_usuario_inicial(estado_dao, cidade_dao, perfil_dao, usuario_dao, nome, email, senha):

    if usuario_dao.get_all():
        return None

    estado = obter_ou_criar_estado(estado_dao)
    cidade = obter_ou_criar_cidade(cidade_dao, estado)
    perfil = obter_ou_criar_perfil_administrador(perfil_dao)

    usuario = Usuario(
        None,
        nome,
        email,
        date.today(),
        cidade,
        perfil,
        Senha_Utils.gerar_hash(senha)
    )

    return usuario_dao.save(usuario)


def main():

    database = Database()

    estado_dao = Estado_DAO(database)
    cidade_dao = Cidade_DAO(database, estado_dao)
    perfil_dao = Perfil_DAO(database)
    usuario_dao = Usuario_DAO(database, cidade_dao, perfil_dao)

    if usuario_dao.get_all():
        print("Já existem usuários cadastrados. Seed não é necessário.")
        return

    print("=== Criação do usuário administrador inicial ===")
    nome = input("Nome: ")
    email = input("E-mail: ")
    senha = getpass.getpass("Senha: ")

    if not nome or not email or not senha:
        print("Nome, e-mail e senha são obrigatórios. Seed cancelado.")
        return

    usuario = criar_usuario_inicial(
        estado_dao,
        cidade_dao,
        perfil_dao,
        usuario_dao,
        nome,
        email,
        senha
    )

    print()
    print(f"Usuário administrador criado com sucesso: {usuario.email}")
    print("Já pode fazer login na aplicação com essas credenciais.")


if __name__ == "__main__":
    main()
