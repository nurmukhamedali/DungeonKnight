from abc import ABC, abstractmethod
import pygame
import random
from .hero import Hero
from .interactive import Interactive
from .creature import Creature
from .abstract import AbstractObject
from .ally import Ally
from .enemy import Enemy


def create_sprite(img, sprite_size):
    icon = pygame.image.load(img).convert_alpha()
    icon = pygame.transform.scale(icon, (sprite_size, sprite_size))
    sprite = pygame.Surface((sprite_size, sprite_size), pygame.HWSURFACE)
    sprite.blit(icon, (0, 0))
    return sprite


