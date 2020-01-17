'''
Created on Jun 5, 2011

@author: robertsavannah
'''
from types import ListType, StringType, IntType
from exceptions import TypeError

class PI_Recipe(object):
    """Class defining Eve Online Planetary Interaction recipes"""
    def __init__(self, name, output, input, mat_level = 'P1'):
        """Constructor"""        
        if not ListType == type(input):
            raise TypeError('input must be a list')
        
        if not StringType == type(name):
            raise TypeError('name must be a string')
        
        if not IntType == type(output):
            raise TypeError('output must be an integer')
        
        if not StringType == type(mat_level):
            raise TypeError('mat_level must be a string')
        
        self._name = name
        self._input = input
        self._output = output
        self._mat_level = mat_level
    
    def __repr__(self):
        repr_str = '-%s- recipe' % self._name.upper()
        for item in self._input:
            repr_str = '%s\n-- %d %s' % (repr_str, item[1], item[0].upper())
        return repr_str
    
    def Mat_List(self, quantity_needed = 1, mat_level = None):
        cycles = (quantity_needed / self._output + 1,
                  quantity_needed / self._output)[0 == quantity_needed % self._output]
        
#        needed = [(cycles * sub[1], sub[0].upper()) for sub in self._input]
        needed = []
        for sub in self._input:
            needed.append((sub[0].upper(), cycles * sub[1], sub[2] and sub[2]._mat_level or 'P0'))
            if PI_Recipe == type(sub[2]):
                needed.extend(sub[2].Mat_List(cycles * sub[1]))
        
        mats_list = mat_level and [n for n in needed if mat_level == n[2]] or needed
        mats_list.sort()
        
        return mats_list


def list_to_dict(mat_list):
    if ListType != type(mat_list):
        return dict()
    
    d = dict()
    mat_list.sort()
    for item in mat_list:
        if item[0] not in d.keys():
            d.update({item[0]: item})
        else:
            d.update({item[0]: (d[item[0]][0],
                                d[item[0]][1] + item[1],
                                d[item[0]][2])})
    
    return d