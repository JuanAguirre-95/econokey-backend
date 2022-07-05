from flask import Blueprint, request
from app.services.generators.generator_service import GeneratorService

gen_view = Blueprint("gen_view", __name__, url_prefix="/generate")

gen = GeneratorService([".password", ".passphrase", ".wallet"])


def validate_json_body(body: dict):
    pass


@gen_view.post("/")
def generate():
    """
    Instantiates a generator with the specified parameters that are included in the request body and returns the
    generated results.
    :return: JSON
    """
    payload = request.get_json()
    validate_json_body(payload)
    generator = gen.create_generator(payload)
    return generator.generate()

