# coding=utf-8

import xml.etree.ElementTree as ET
import pickle
import requests
import time
from lxml import html
import sys, json
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

from zeep import Client 

reload(sys)
sys.setdefaultencoding('utf-8')


################################################################################################

def clear_atm(category):

	category = [i.replace('\n','') for i in category]
	
	category = [i.strip(' ') for i in category if len(i) > 3 and not None]

	return filter(None,category)

################################################################################################
def get_atm(tree):

	data = {}

	# Activity Category
	try:
		x = tree.xpath('//div[contains(@class,"field-name-field-atm-activity-category")]/div/descendant::*/text()')
		

		data['actCategory'] = x
	except:
		data['actCategory'] = None		
		print 'except','ATM activity category'

	#ATM data category
	try:
		x = tree.xpath('//div[contains(@class,"field-name-field-atm-data-category")]/div/descendant::*/text()') 

		data['dataCategory'] = x

	except:
		data['dataCategory'] = None
		print 'except', 'ATM data category'

	#Atm stakeholders 
	try:

		x = tree.xpath('//div[contains(@class,"field-name-field-atm-stakeholders")]/div/descendant::*/text()')


		data['dataStakeholder'] = x
	except:
		data['dataStakeholder'] = None
		print 'except', 'Atm stakeholders'

	#atm regions 
	try:

		x = tree.xpath('//div[contains(@class,"field-name-field-regions")]/div/descendant::*/text()')
		data['regions'] = x

	except:
		data['regions'] = None
		print 'Except','Regioes'  

	#atm flight phases
	try:
		x = tree.xpath('//div[contains(@class,"field-name-field-flight-phases")]/div/descendant::*/text()')

		data['flightPhases'] = x
	except:
		data['flightPhases'] = None
		print 'Except','atm flight phases'

	return data


################################################################################################

def get_header(tree):
	
	data = {}

	try:

		name = tree.xpath('//div[contains(@class,"page-header")]/h1/text()') 
		name = [i.replace('\t','') for i in name]
		data['nameService'] = clear_atm(name)[0]

		per_describe = tree.xpath('//div[@class="percent-complete"]/text()')
		data['percentPrescribe'] =  per_describe[0]
		
	except:
		data['percentPrescribe'] = None
		print 'Exception', 'NOME SERVICO'

	try:
	
		version = tree.xpath('//*[@id="block-system-main"]/div/div/div/div[1]/div/div[2]/div/div[1]/div/div/div/div[1]/div/div/div[2]/div/text()')

		data['version'] = version[0]

		implementStatus = tree.xpath('//*[@id="block-system-main"]/div/div/div/div[1]/div/div[2]/div/div[1]/div/div/div/div[5]/div/div/div[2]/div/text()')

		data['implementStatus'] = implementStatus[0]
	except:
		print 'Exception', 'VERSAO Servico'
		data['implementStatus'] = None

	try:
		versionCategory  = tree.xpath('//*[@id="block-system-main"]/div/div/div/div[1]/div/div[2]/div/div[1]/div/div/div/div[7]/div/div/div[2]/div/text()')
		data['versionCategory'] = versionCategory[0]

	except:
		data['versionCategory'] =None
		print 'Exception', 'Categoria Versao'

	return data

################################################################################################

def get_registrationProcess(tree):
	
	data = {}

	#Service Description
	try:
	
		serviceDescription = tree.xpath('//div[@id="rmjs-1"]/descendant::*/text()')
		
		data['serviceDescription'] = serviceDescription
	except:
		data['serviceDescription'] = None
		print 'Except', 'Service Description'

	# Service Tecnical Interface
	try:
		serviceTecnicalInterface = tree.xpath('//*[@id="block-system-main"]/div/div/div/div[3]/div/div[2]/div/div[1]/div/div/div/div[3]/div/div/div/div/div/div[2]/div/div/descendant::*/text()')
		
		data['serviceTecnicalInterface'] = serviceTecnicalInterface
	except:
		data['serviceTecnicalInterface'] = None
		print 'Except', 'Service Tecnical Interface'
	
	return data
################################################################################################

def plot_node(node):
	print len(node)
	if len(node) > 1:
		for n in node.getiterator():
			plot_node(n)
	else:
		print  node.tag, node.text, node.attrib
		return

################################################################################################  

baseurl  ='https://eur-registry.swim.aero'

driver  = webdriver.Chrome('/usr/local/share/chromedriver')

driver.get('https://eur-registry.swim.aero/user/login')

username = driver.find_element_by_id("edit-name")
password = driver.find_element_by_id("edit-pass")

username.send_keys("camilacb@icea.gov.br")
password.send_keys("Camil@01")

driver.find_element_by_id("edit-submit").click()

time.sleep(5)

pages = '/service-implementations?sid=All&field_version_category_tid=All&title=&body_value=&&&&&&&&page='

data_json = {}

j = 0
	

dataServices = {}
for k in xrange(0,3): #Numero de paginas
	
	driver.get(baseurl+pages+str(k))

	time.sleep(1)

	tree = html.fromstring(driver.page_source)

	s = tree.xpath('//a/@href')

	ss = [x for x in s if '/services/' in x]

	services = []
	for i in ss:
		if i not in services:
			services.append(i)

	print services, len(services)
	
	for i in services:

		driver.get('https://eur-registry.swim.aero/services/eurocontrol/flightfilingservice-195')#baseurl+i)	
	
		time.sleep(1)

		tree = html.fromstring(driver.page_source)

		ak = driver.find_elements_by_xpath('//*[@id="block-system-main"]/div/div/div/div[3]/div/div[2]/div/div[1]/div/div/div/div[3]/div/div/div/div/div/div[2]/div/span/span/a')

		print 'link',ak

		if len(ak) > 0:
			ak[0].click()

			aj = driver.find_elements_by_xpath('//*[@id="block-system-main"]/div/div/div/div[3]/div/div[2]/div/div[3]/div/div/div/div/div/div[2]/div/span[1]/span/a')
			
			if len(aj) > 0:
			
				aj[0].click()
				
				ah = driver.find_elements_by_xpath('//*[@id="block-system-main"]/div/div/div/div[1]/div/div[2]/div/div[3]/div/div/div[2]/div/span/a')

				if len(ah) > 0:

					ah[0].click()

					doc = driver.find_element_by_xpath('/html/body').text

					wer = ET.ElementTree(ET.fromstring(doc))

					tree = (ET.tostring(wer.getroot()))
	
					root = wer.getroot()

					ax = root.findall('.//{http://schemas.xmlsoap.org/wsdl/}portType')
					
					dataServices[i] = {}
					for moc in ax:
						
						print 'moc', len(moc)

						

						for node in moc.getiterator():
							#print  'node' #,   node, len(node)
							print 'node', node.attrib, node.tag

							
							
							for child in node.getiterator():

								#if(child.attrib.keys()[0] == 'name'):
								#	if()child.attrib['name'] == 'portType'
									
								
								#print 'child ',child, len(child)
								print 'child',  child.attrib.keys()[0], child.tag[-9:], 'operation' in child.tag[-12:], 'portType' in child.tag[-12:]  
							
	
					#print ax[0].text#tree.xpath('//portType/')

					driver.close()

					sys.exit()
		

		#data_json[j] = {'header':get_header(tree), 'atm':get_atm(tree),'registrationProcess':get_registrationProcess(tree)}

		j+=1

		print j

#with open('resultado.json','w') as out:
#	json.dump(data_json,out)
	
#with open('Output.txt' ,'w') as te:
#	te.write(driver.page_source)



#with open('Output.txt','w') as text_file:
#	text_file.write(page.text)


