import random
from collections import defaultdict
from typing import List


class Entity:
    def __init__(self, name:str, score:int):
        self.name = name
        self.score = score

    def __str__(self):
        return '{} ({})'.format(self.name, self.score)


def binary_search(a, x):
    # TODO make binary
    if x <= a[0]:
        return a[0]
    for e in a:
        if e >= x:
            return e
    return a[-1]


class EntityContainer:
    def __init__(self, name:str, c:int, entity_list:List[Entity] = None):
        if entity_list is None:
            entity_list = []
        self.name = name
        self.c = c
        self.entity_list = entity_list
        self.index = defaultdict(list)
        self.scores = []
        self.build_index()

        # TODO
        # self.c = 1

    def append(self, entity: Entity):
        self.entity_list.append(entity)
        self._add_to_index(entity)
        # TODO lol
        self.scores = sorted(list(self.index.keys()))

    def build_index(self):
        for e in self.entity_list:
            self._add_to_index(e)
        self.scores = sorted(list(self.index.keys()))

    def peek_nearest(self, score:int) -> Entity:
        if score not in self.index:
            score = binary_search(self.scores, score)
        return random.choice(self.index[score])

    def _add_to_index(self, entity:Entity):
        self.index[entity.score].append(entity)

