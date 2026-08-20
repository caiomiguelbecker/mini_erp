import hashlib
import secrets


class Senha_Utils:

    @staticmethod
    def gerar_hash(senha_texto_plano):
        salt = secrets.token_hex(16)
        hash_senha = hashlib.sha256(
            (salt + senha_texto_plano).encode("utf-8")
        ).hexdigest()
        return f"{salt}${hash_senha}"

    @staticmethod
    def verificar_senha(senha_texto_plano, senha_armazenada):
        salt, hash_esperado = senha_armazenada.split("$")
        hash_calculado = hashlib.sha256(
            (salt + senha_texto_plano).encode("utf-8")
        ).hexdigest()
        return hash_calculado == hash_esperado
