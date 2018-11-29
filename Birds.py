#!/bin/python3

import math
import os
import random
import re
import sys
from collections import OrderedDict

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    sited = dict()
    currentmax = 0
    maxindex = -1

    for bird in arr:
        if bird not in sited:
            sited[bird] = 1
        else:
            sited[bird] += 1

    orderedbirds = OrderedDict(**sited.items)
    for bird in orderedbirds.keys():
        if orderedbirds[bird] > currentmax:
            currentmax = sited[bird]
            maxindex = bird
    return maxindex

if __name__ == '__main__':

    arr_count = int(input('array size: ').strip())

    arr = list(map(int, input('array string: ').rstrip().split()))

    result = migratoryBirds(arr)

    print(f'{result} has the most sightings')
