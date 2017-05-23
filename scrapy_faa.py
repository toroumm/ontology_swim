
import json, os, sys, time

from lxml import html
from selenium import webdriver

reload(sys)
sys.setdefaultencoding('utf-8')


#################################################################################
def get_header(tree):
	data = {}

	try:
		serviceName = tree.xpath('//*[@id="post-content"]/div/div[2]/div/h4[1]/span/text()')
		data['serviceName'] = serviceName
	except:

		data['serviceName'] = None
		print 'Expcept : ', 'Service Name'

	try:
		
		lifeCicleStage = tree.xpath('//*[@id="post-content"]/div/div[1]/div[1]/div/div/div/div/div/div/em/text()')
		data['lifeCicleStage'] = lifeCicleStage
	except:
		data['lifeCicleStage'] = None
		print 'Expcept : ', 'Life cicle Stage'

	try:

		serviceCategory = tree.xpath('//*[@id="post-content"]/div/div[2]/div/h4[6]/span/text()')
		data['serviceCategory'] = serviceCategory

	except:
		data['serviceCategory'] = None
		print 'Expcept : ','Service Category'

	try:
		
		serviceCriticalLevel = tree.xpath('//*[@id="post-content"]/div/div[2]/div/h4[9]/span/text()')
		data['serviceCriticalLevel'] = serviceCriticalLevel
	except:
		serviceCriticalLevel = None
		print 'Expcept : ', 'Service Critical Level'
	
	try:
		serviceDescription = tree.xpath('//*[@id="post-content"]/div/div[2]/div/h4[2]/span/p/text()')
		data['serviceDescription'] = serviceDescription
	except:
		data['serviceDescription'] = None
		print 'Expcept : ', 'Service Description'

				
	try:	
		serviceVersion = tree.xpath('//*[@id="post-content"]/div/div[2]/div/h4[4]/span/text()')
		data['serviceVersion'] = serviceVersion

	except:
		data['serviceVersion'] = None
		print  'Expcept : ', 'Service Version'


	try:
		messagingModel = tree.xpath('//*[@id="post-content"]/div/div[2]/div/h4[8]/span/text()')	
		data['messagingMode'] = messagingModel
	except:
		data['messaging'] = None
		print 'Expcept : ','Messaging Mode'
	
	try:

		interfaceType = tree.xpath('//*[@id="post-content"]/div/div[2]/div/h4[7]/span/text()')
		data['interfaceType'] = interfaceType
		
	except:
		
		data['interfaceType'] = None

		print 'Expcept : ', 'Interface Type'

	try:
		atmServiceCategory = tree.xpath('//*[@id="post-content"]/div/div[2]/div/h4[5]/span/text()')
		data['atmServiceCategory'] = atmServiceCategory
	except:
		data['atmServiceCategory'] = None
		print 'Expcept : ', 'ATM Service Category'
	
	return data

#################################################################################
def get_provider_name(tree,driver):

	data = {}
			
	for ii in tree:
		if '/spsf' in ii:
				
			print ii
			driver.get(base_url+ ii)
			
			time.sleep(5)
						
			tr = html.fromstring(driver.page_source)

			try:

				serviceProviderName = tr.xpath('//*[@id="post-content"]/div/div[2]/div/h4[1]/span/text()')
				data['serviceProviderName'] = serviceProviderName
			except:
				data['serviceProviderName'] = None

				print 'Exception ',' Service Provide Name'

			break
	return data

#################################################################################

def get_security(tree,driver):		

	'''
		Ainda falta o security Mechanisms
	'''	
	
	data = {}

	for ii in tree:
		if '/security' in ii:
			
			print ii 

			driver.get(base_url+ ii)

			time.sleep(5)
						
			tr = html.fromstring(driver.page_source)

			try:

				security = tr.xpath('//*[@id="post-content"]/div/div[2]/div/h4[1]/div/p/text()')
				data['securityDescription'] = security
			except:
				data['securityDescription'] = None

				print 'Exception ',' Security Description'

			break

	return data

#################################################################################

'''
Esse tem que analizar com calma, alem da tabelas os Qos Parameters podem ter diversos forms

Vou realmente deixar para a 2 fase

'''

def get_qos(tree, driver):	#Quality of services (qos)
	data = {}


	for ii in tree:
		if '/qos' in ii:
			
			print ii 

			driver.get(base_url+ ii)

			time.sleep(5)
						
			tr = html.fromstring(driver.page_source)

			try:

				qosDescription = tr.xpath('//*[@id="post-content"]/div/div[2]/div/h4[1]/div/text()')
				data['qosDescription'] = qosDescription
			except:
				data['qosDescription'] = None

				print 'Exception ',' QOS Description'

			try:

				qosParameterName = tr.xpath('//*[@id="post-content"]/div/div[2]/div/h4[2]/span/div/div[1]/div[1]/h4[1]/span/text()')
				data['qosParameterName'] = qosParameterName
			except:
				data['qosParameterName'] = None

				print 'Exception ',' QOS Parameter Name'


			try:

				qosParameterDefinition = tr.xpath('//*[@id="post-content"]/div/div[2]/div/h4[2]/span/div/div[1]/div[1]/h4[1]/span/text()')
				data['qosParameterName'] = qosParameterName
			except:
				data['qosParameterName'] = None

				print 'Exception ',' QOS Parameter Name'

			break
			
			


	return data
#################################################################################

def get_implementation(tree, driver):

	data = {}
	
	for ii in tree:
		if '/implementation' in ii:
			
			print ii 

			driver.get(base_url+ ii)

			time.sleep(5)
						
			tr = html.fromstring(driver.page_source)

			try:

				implementationName = tr.xpath('//*[@id="post-content"]/div/div[2]/div/span/span/h3/em/text()')
				data['implementationName'] = implementationName
			except:
				data['implementationName'] = None

				print 'Exception ',' Implementation Name'


			try:

				implementationDescrition = tr.xpath('//*[@id="post-content"]/div/div[2]/div/h4[1]/div/p/text()')
				data['implementationDescrition'] = implementationDescrition
			except:
				data['implementationDescrition'] = None

				print 'Exception ',' Implementation Description'

			break
	return data

	

#################################################################################
base_url = 'https://nsrr.faa.gov'

driver = webdriver.Chrome('/usr/local/share/chromedriver')
driver.get(base_url)

username = driver.find_element_by_id('edit-name')
password = driver.find_element_by_id('edit-pass')

username.send_keys('coloque o usuario')

password.send_keys('coloque a senha')

driver.find_element_by_id('edit-submit').click()

data_json = {}

k = 0

for i in range(0,10):

	driver.get(base_url+'/?title=&page='+str(i))

	tree = html.fromstring(driver.page_source)
	
	s = tree.xpath('//a/@href')

	ss = [x for x in s if '/services/' in x]
	
	for j in ss:

		data_json[k] ={}
	
		driver.get(base_url+j)

		time.sleep(5)

		dwe = html.fromstring(driver.page_source)

		data_json[k]['header'] = get_header(dwe)

		services = html.fromstring(driver.page_source)

		treeService = services.xpath('//a/@href')

		data_json[k]['security'] = get_security(treeService,driver)
		
		data_json[k]['provider'] = get_provider_name(treeService,driver)

		data_json[k]['implementation'] = get_implementation(treeService,driver)

		k+=1

		print k
	
with open('faaServices.json','w') as jq:
	json.dump(data_json,jq)		

#################################################################################



