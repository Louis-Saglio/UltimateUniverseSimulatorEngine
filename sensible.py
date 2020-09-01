from typing import List


class SensType:
    pass


class SensoryOrgan:
    def __init__(self, sens_type: SensType):
        self.type = sens_type

    def receive_data(self, data):
        pass


class Sensible:
    def __init__(self, sensory_organs: List[SensoryOrgan]):
        self.sensory_organs = sensory_organs
