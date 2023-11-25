from tree import RGBXmasTree
from colorzero import Color

tree = RGBXmasTree()

try:
    tree.color = Color('blue')
except KeyboardInterrupt:
    tree.close()