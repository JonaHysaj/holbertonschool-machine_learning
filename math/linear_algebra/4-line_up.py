#!/usr/bin/env python3
'''LIne up'''


def add_arrays(vec1, vec2):
    '''testttttt'''
    result = []
    if(len(vec1) != len(vec2)):
        return None
    else:
        for i in vec1:
            result.append(vec1[i-1] + vec2[i-1])
        return result


arr1 = [1, 2, 3, 4]
arr2 = [5, 6, 7, 8]
add_arrays(arr1, arr2)
arr1
arr2
add_arrays(arr1, [1, 2, 3])
