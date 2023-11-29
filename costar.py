from colorzero import Color
from tree import RGBXmasTree
import random

tree = RGBXmasTree()

costar_colors = [Color('red'), Color('blue'), Color('green'), Color.from_rgb(1.0, 0.34, 0.2)]

try:
    while True:
        pixel = random.choice(tree)
        pixel.color = random.choice(costar_colors)
except KeyboardInterrupt:
    tree.off()
    tree.close()
