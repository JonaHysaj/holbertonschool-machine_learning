#!/usr/bin/env python3
import numpy as np
'''Cat got your tounge '''


def np_cat(mat1, mat2, axis=0):
    '''Cat got your tounge'''
    arr = np.concatenate((mat1, mat2), axis=axis)
    return arr
