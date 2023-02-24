#!/usr/bin/env python3
import numpy as np
'''Cat gotn'''


def np_cat(mat1, mat2, axis=0):
    '''Cat got fn'''
    arr = np.concatenate((mat1, mat2), axis=axis)
    return arr
