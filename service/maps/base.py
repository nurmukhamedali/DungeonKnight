import yaml
from abc import ABC


class MapFactory(yaml.YAMLObject):

    @classmethod
    def from_yaml(cls, loader, node):

        # FIXME
        # get _map and _obj
        _map = cls.get_map()
        _obj = cls.get_object()
        # config = loader.construct_mapping(node)
        # _obj.config.update(config)

        return {'map': _map, 'obj': _obj}

    @classmethod
    def get_map(cls):
        return cls.Map()

    @classmethod
    def get_object(cls):
        return cls.Objects()

    class Map(ABC):
        pass

    class Objects(ABC):
        pass

