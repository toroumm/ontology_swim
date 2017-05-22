
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

base_url = 'https://nsrr.faa.gov/'

driver = webdriver.Chrome('/usr/local/share/chromedriver')
driver.get(base_url)

username = driver.find_element_by_id('edit-name')
password = driver.find_element_by_id('edit-pass')

username.send_keys('camilacb@icea.gov.br')

password.send_keys('Camil@01')

driver.find_element_by_id('edit-submit').click()

for i in range(1,10):

	tree = html.fromstring(driver.page_source)
	
	s = tree.xpath('//a/@href')

	ss = [x for x in s if '/services/' in x]
	
	for j in ss:
	
		driver.get(base_url+j)

		time.sleep(5)

		dwe = html.fromstring(driver.page_source)

		get_header(dwe)
	
		sys.exit()

#################################################################################



