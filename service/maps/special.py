from .base import MapFactory
from .. import wall, floor1, floor2, floor3



class SpecialMap(MapFactory):
    yaml_tag = "!special_map"

    class Map:
        def __init__(self):
            self.Map = [[0 for _ in range(41)] for _ in range(41)]


        def get_map(self):
            return self.Map


    class Objects:
        def __init__(self):
            self.objects = []

        def get_objects(self, _map):
            return self.objects


