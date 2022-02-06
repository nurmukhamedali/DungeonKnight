import random
from .base import MapFactory
from .. import wall, floor1, floor2, floor3


class RandomMap(MapFactory):
    yaml_tag = "!random_map"

    class Map:

        def __init__(self):
            self.Map = [[0 for _ in range(41)] for _ in range(41)]
            for i in range(41):
                for j in range(41):
                    if i == 0 or j == 0 or i == 40 or j == 40:
                        self.Map[j][i] = wall
                    else:
                        self.Map[j][i] = [wall, floor1, floor2, floor3, floor1,
                                          floor2, floor3, floor1, floor2][random.randint(0, 8)]

        def get_map(self):
            return self.Map

    class Objects:

        def __init__(self):
            self.objects = []

        def get_objects(self, _map):

            for obj_name in object_list_prob['objects']:
                prop = object_list_prob['objects'][obj_name]
                for i in range(random.randint(prop['min-count'], prop['max-count'])):
                    coord = (random.randint(1, 39), random.randint(1, 39))
                    intersect = True
                    while intersect:
                        intersect = False
                        if _map[coord[1]][coord[0]] == wall:
                            intersect = True
                            coord = (random.randint(1, 39),
                                     random.randint(1, 39))
                            continue
                        for obj in self.objects:
                            if coord == obj.position or coord == (1, 1):
                                intersect = True
                                coord = (random.randint(1, 39),
                                         random.randint(1, 39))

                    self.objects.append(Objects.Ally(
                        prop['sprite'], prop['action'], coord))

            for obj_name in object_list_prob['ally']:
                prop = object_list_prob['ally'][obj_name]
                for i in range(random.randint(prop['min-count'], prop['max-count'])):
                    coord = (random.randint(1, 39), random.randint(1, 39))
                    intersect = True
                    while intersect:
                        intersect = False
                        if _map[coord[1]][coord[0]] == wall:
                            intersect = True
                            coord = (random.randint(1, 39),
                                     random.randint(1, 39))
                            continue
                        for obj in self.objects:
                            if coord == obj.position or coord == (1, 1):
                                intersect = True
                                coord = (random.randint(1, 39),
                                         random.randint(1, 39))
                    self.objects.append(Objects.Ally(
                        prop['sprite'], prop['action'], coord))

            for obj_name in object_list_prob['enemies']:
                prop = object_list_prob['enemies'][obj_name]
                for i in range(random.randint(0, 5)):
                    coord = (random.randint(1, 30), random.randint(1, 22))
                    intersect = True
                    while intersect:
                        intersect = False
                        if _map[coord[1]][coord[0]] == wall:
                            intersect = True
                            coord = (random.randint(1, 39),
                                     random.randint(1, 39))
                            continue
                        for obj in self.objects:
                            if coord == obj.position or coord == (1, 1):
                                intersect = True
                                coord = (random.randint(1, 39),
                                         random.randint(1, 39))

                    self.objects.append(Objects.Enemy(
                        prop['sprite'], prop, prop['experience'], coord))

            return self.objects
