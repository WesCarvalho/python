import json
from flask import Blueprint, Response, request

from model.Usuario import Usuario

usuario_controller = Blueprint('usuario_controller', __name__)


@usuario_controller.route('/login', methods=["POST"])
def login():
    parametros = request.get_json()
    resposta = {
        "mensagem": ""
    }
    usuario = Usuario(parametros["usuario"], parametros["senha"])

    if (usuario.nome == "Weslley" and usuario.senha == "12345"):
        usuario.token = "KSHDAKJ5454JFDJ434O"
        return Response(json.dumps(usuario.__dict__), status=200, mimetype="application/json")
    else:
        resposta["mensagem"] = "Usuario ou senha inconrreto."

    return Response(json.dumps(resposta), status=401, mimetype="application/json")
