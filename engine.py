from typing import List

from entity import RealTimeEntity


class RealTimeEngine:
    def __init__(self, entities: List[RealTimeEntity]):
        self.entities = entities

    def run(self):
        for entity in self.entities:
            entity.run()
        for entity in self.entities:
            entity.update()