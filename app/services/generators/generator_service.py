"""
Generator Module
"""
from typing import Any

from app.services.generators import factory, loader
from app.services.generators.strategies.base import BaseGenerator


class GeneratorService:
    """
    Generator factory
    """

    def __init__(self, generator_list: list[str], *args, **kwargs):
        self.loader = loader
        self.loader.load_plugins(generator_list)

    def create_generator(self, parameters: dict[str:Any], *args, **kwargs) -> BaseGenerator:
        return factory.create(parameters)

    def get_generators(self):
        return factory.get_funcs()

