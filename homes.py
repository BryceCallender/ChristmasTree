from tree import RGBXmasTree
from colorzero import Color

tree = RGBXmasTree()

try:
    tree.color = Color('orange')
except KeyboardInterrupt:
    tree.close()