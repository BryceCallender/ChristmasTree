from colorzero import Color
from tree import RGBXmasTree
import random

tree = RGBXmasTree()

costar_colors = [Color('red'), Color('blue'), Color('green'), Color('#FF5733')]

try:
    while True:
        pixel = random.choice(tree)
        pixel.color = random.choice(costar_colors)
except KeyboardInterrupt:
    tree.off()
    tree.close()
