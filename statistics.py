
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
			a, b = None, None
			for ddd in _dict[d][dd]:

				if ddd == strL1:
					if len(_dict[d][dd][ddd]) > 0:
						a = [_l1.index(x) for x in _dict[d][dd][ddd]]

				elif ddd == strL2:
					if len(_dict[d][dd][ddd]) > 0:
						b = [_l2.index(x) for x in _dict[d][dd][ddd]]

			try:
				if type(a) is list and type(b) is list:
					for ii in a:
						for jj in b:
							arr[ii,jj]+=1
					#arr[a,b] +=1
			except:
				print a, b
				#print arr
				print 'parou', arr.shape
				#sys.exit()
	total_rows = np.sum(arr, axis=1)
	per_total_rows = total_rows / np.sum(total_rows)

	arr = np.concatenate((arr,total_rows.reshape(total_rows.shape[0],1), per_total_rows.reshape(per_total_rows.shape[0],1)),axis=1)

	total_cols = np.sum(arr, axis=0)
	per_total_cols = total_cols / np.sum(total_cols)

	arr = np.concatenate(
		(arr, total_cols.reshape(1,total_cols.shape[0]), per_total_cols.reshape(1,per_total_cols.shape[0])), axis=0)

	_l2 = _l2 + ['Total', '%Total']

	_l1 = _l1 + ['Total', '%Total']

	df = pandas.DataFrame(arr, columns=_l2, index=_l1)

	df.to_csv(path_to_save + strL1+'_and_'+strL2+'.csv')

	return arr,df
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

	return arr,df

#*****************************************************************************

_file = 'eurServices.json'

with open(_file) as f:
	onto = json.load(f)

path_to_save = 'eurControlTables/'


#a,b = getTableStatistic('actCategory','dataCategory',onto,path_to_save)

#t =  b['%Total'][:-2]

#w = b['Total'].values

#t.plot(kind = 'scatter',subplots= True)

#plt.show()

'''
getTableStatistic('actCategory','dataCategory',onto,path_to_save)

getTableStatistic('regions','dataCategory',onto,path_to_save)

getTableStatistic('regions','actCategory',onto,path_to_save)

getTableStatistic('actCategory','dataStakeholder',onto,path_to_save)

getListStatistics('implementStatus',onto,path_to_save)

getListStatistics('regions',onto,path_to_save)

'''

getListStatistics('dataCategory',onto,path_to_save)