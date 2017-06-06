
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

'''


#*****************************************************************************

_file = 'eurServices.json'

with open(_file) as f:
	onto = json.load(f)

path_to_save = 'eurControlTables/'


getTableStatistic('actCategory','dataCategory',onto,path_to_save)

getTableStatistic('regions','dataCategory',onto,path_to_save)

getTableStatistic('regions','actCategory',onto,path_to_save)

getTableStatistic('actCategory','dataStakeholder',onto,path_to_save)


'''
#regions = getItemList(onto, 'regions')

#dataCategory = getItemList(onto,'dataCategory')

#actCategory = getItemList(onto,'actCategory')

#dataStakeholder = getItemList(onto,'dataStakeholder')

df =  pandas.DataFrame(getTableStatistic('actCategory','dataCategory',onto), columns=dataCategory,index=actCategory)

df.to_csv(path_to_save+'eur-act_and_dataCategory.csv')

de = pandas.DataFrame(getTableStatistic('regions','dataCategory',onto),columns=dataCategory,index=regions)

de.to_csv(path_to_save+'eur-data_and_regions.csv')

dt = pandas.DataFrame(getTableStatistic('regions','actCategory',onto),columns=actCategory,index =regions)

dt.to_csv(path_to_save+'eur-act_and_regions.csv')

dw = pandas.DataFrame(getTableStatistic('actCategory','dataStakeholder',onto),columns=dataStakeholder, index= actCategory)

dw.to_csv(path_to_save+'eur-stakeholder_and_act.csv')

'''

