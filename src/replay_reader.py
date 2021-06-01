import numpy as np

from other import parse

path = r'replays\14612289.fafreplay'

with open(path, "rb") as fh:
    data = fh.read()

parse(data)
