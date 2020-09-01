class Entity:
    def run(self):
        raise NotImplementedError


# noinspection PyAbstractClass
class RealTimeEntity(Entity):
    _next_state_cache = {}

    def __setattr__(self, key, value):
        self._next_state_cache[value] = key

    def update(self):
        for key, value in self._next_state_cache.items():
            super(RealTimeEntity, self).__setattr__(key, value)
