from flask import Blueprint, request, jsonify
from app.services.generators.generator_service import GeneratorService
from typing import get_type_hints
generators_view = Blueprint("generators_view", __name__, url_prefix="/generators")

gen = GeneratorService([".password", ".passphrase", ".wallet_btc"])

@generators_view.get("/")
def generate():
    """

    :return: JSON
    """
    ret = []
    generators = gen.get_generators()
    for elem in generators:
        gen_func = generators[elem]
        gnrtr = gen_func()
        hints = gnrtr.get_defaults()

        gen_ret = {
            "generator_type": gnrtr.generator_type,
            "generator_defaults": hints
        }
        ret.append(gen_ret)
    print(ret)
    return jsonify(ret)