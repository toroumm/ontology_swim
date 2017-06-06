
import numpy as np
import matplotlib.pyplot as plt
import os, json, sys
import csv

#*****************************************************************************

'''
Retorna uma lista com os itens da key em cada servico

_dict  = json ontologia

key = chave especifica que e pesquisada em todos os serviços

'''

def getItemList(_dict, key):
	_list = []
	for d in _dict:
		for dd in _dict[d]:
			control = False
			for ddd in _dict[d][dd]:
				#print ddd, key
				if  key == ddd and len(_dict[d][dd][ddd]) > 0:
					x = set(_list)
					y = set(_dict[d][dd][ddd])

					k = y - x

					_list = _list + list(k)
					control = True
					break
			if(control):
				break
	return _list
#*****************************************************************************
'''
Retorn uma matrix com a intercção de duas chaves

strL1 = key1

strL2 = key2

_dict = json ontologia

'''
def getTableStatistic(strL1, strL2, _dict):

	_l1 = getItemList(_dict,strL1)

	_l2 = getItemList(_dict,strL2)

	arr = np.zeros((len(_l1),len(_l2)))

	for d in _dict:
		for dd in _dict[d]:
			for ddd in _dict[d][dd]:
				a,b = 1,1
				if ddd == strL1:
					if len(_dict[d][dd][ddd]) > 0:
						a = [_l1.index(x) for x in _dict[d][dd][ddd]]

				elif ddd == strL2:
					if len(_dict[d][dd][ddd]) > 0:
						b = [_l2.index(x) for x in _dict[d][dd][ddd]]
				arr[a,b] +=1
	return arr
#*****************************************************************************

_file = 'resultado.json'

with open(_file) as f:
	onto = json.load(f)


regions = getItemList(onto, 'regions')

dataCategory = getItemList(onto,'dataCategory')

actCategory = getItemList(onto,'actCategory')

print regions
print dataCategory
print actCategory

print getTableStatistic('actCategory','dataCategory',onto)



