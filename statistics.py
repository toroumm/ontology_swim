
# coding=utf-8

import numpy as np
import matplotlib.pyplot as plt
import os, json, sys
import csv,pandas

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
				ok = False
				if type(_dict[d][dd][ddd]) is list:
					if len(_dict[d][dd][ddd]):
						ok = True
				else:
					if(_dict[d][dd][ddd] is not None):
						ok = True
				if  key == ddd and ok:
					if type(_dict[d][dd][ddd]) is list:
						x = set(_list)
						y = set(_dict[d][dd][ddd])

						k = y - x

						_list = _list + list(k)
					elif type(_dict[d][dd][ddd]) is not list and _dict[d][dd][ddd] not in _list :
						_list.append(_dict[d][dd][ddd])
					control = True
					break
			if(control):
				break
	return _list
#*****************************************************************************
'''
Retorna uma matrix com a intercção de duas chaves

strL1 = key1

strL2 = key2

_dict = json ontologia

'''
def getTableStatistic(strL1, strL2, _dict, path_to_save):

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

	df = pandas.DataFrame(arr, columns=_l2,
						  index=_l1)

	df.to_csv(path_to_save + strL1+'_and_'+strL2+'.csv')

	return arr
#*****************************************************************************

'''
get statistics

Retorna um vetor com a contagem de cada chave por serviço

strL1 = key1

_dict = json ontologia

'''
def getListStatistics(strL1, _dict, path_to_save):

	_list = getItemList(_dict,strL1)

	arr = np.zeros((1,len(_list)))

	for d in _dict:
		for dd in _dict[d]:
			for ddd in _dict[d][dd]:
				a = None

				if ddd == strL1:

					ok = False
					if type(_dict[d][dd][ddd]) is list:
						if len(_dict[d][dd][ddd]):
							ok = True
					else:
						if (_dict[d][dd][ddd] is not None):
							ok = True
					if ok:
						if len(_dict[d][dd][ddd]) > 0 and type(_dict[d][dd][ddd]) is list:
							a = [_list.index(x) for x in _dict[d][dd][ddd]]
						elif _dict[d][dd][ddd] is not None and ok and type(_dict[d][dd][ddd]) is not list:
							a = _list.index(_dict[d][dd][ddd])
				if a is not None:
					arr[0,a] +=1

	df = pandas.DataFrame(arr, columns=_list)

	df.to_csv(path_to_save + strL1+'.csv')

	return arr

#*****************************************************************************

_file = 'eurServices.json'

with open(_file) as f:
	onto = json.load(f)

path_to_save = 'eurControlTables/'


getTableStatistic('actCategory','dataCategory',onto,path_to_save)

getTableStatistic('regions','dataCategory',onto,path_to_save)

getTableStatistic('regions','actCategory',onto,path_to_save)

getTableStatistic('actCategory','dataStakeholder',onto,path_to_save)

getListStatistics('implementStatus',onto,path_to_save)

