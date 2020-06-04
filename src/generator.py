import random
from random import shuffle
from typing import Dict

from model import EntityContainer, Entity


class Distribution:
    def peek_mutation(self):
        pass


class SimpleDistribution(Distribution):
    def __init__(self, dist=None):
        if dist is None:
            dist = [0] * 40 + [1] * 20 + [-1] * 20 + [2] * 10 + [-2] * 10
        self.dist = dist

    def peek_mutation(self) -> int:
        return random.choice(self.dist)


class SimpleGenerator:
    def __init__(self, data:Dict[str, EntityContainer], distribution:Distribution=None):
        if distribution is None:
            distribution = SimpleDistribution()
        self.data = data
        self.distribution = distribution

    def generate(self) -> Dict[str, Entity]:
        result = {}
        keys = list(self.data.keys())
        shuffle(keys)

        k0 = keys[0]
        container = self.data[k0]
        e = random.choice(container.entity_list)
        score = 1. * e.score * container.c
        result[k0] = e

        for key in keys[1:]:
            container = self.data[key]
            chosen_score = round(-score / container.c + self.distribution.peek_mutation())
            e = container.peek_nearest(chosen_score)
            score += e.score * container.c
            result[key] = e
        return result
