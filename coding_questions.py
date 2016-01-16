#! /usr/bin/python

'''These are the solutions to the coding questions provided by
Site Comply.'''

import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from bs4.element import NavigableString


def question_2(list_of_ints):
	
	if any([num < 0 for num in list_of_ints]):
		return 'List must contain only positive integers.'

	contigous_list = [(0, list_of_ints[0])]
	starting_indexes = []

	for index, num in enumerate(list_of_ints[1:], 1):
		if len(contigous_list) == 1:
			if abs(num - contigous_list[0][1]) == 1:
				direction_val = num - contigous_list[0][1]
				contigous_list.append((index, num))
			else:
				contigous_list = [(index, num)]
		else:
			if num - contigous_list[-1][1] == direction_val:
				contigous_list.append((index, num))
			else:
				starting_indexes.append(contigous_list[0][0])
				contigous_list = [(index, num)]
	else:
		if len(contigous_list) > 1:
			starting_indexes.append(contigous_list[0][0])

	return starting_indexes or None


def question_3():

	print '\nretrieving data...\n'
	driver = webdriver.PhantomJS()
	driver.get("http://dbiweb.sfgov.org/dbipts/Default2.aspx?page=addressquery")
	driver.find_element_by_name("InfoReq1$txtStreetNumber").send_keys("555")
	driver.find_element_by_name("InfoReq1$txtStreetName").send_keys("California")
	street_suffix = Select(driver.find_element_by_name('InfoReq1$cboStreetSuffix'))
	street_suffix.select_by_value("ST")
	driver.find_element_by_id("InfoReq1_cmdSearch").click()	
	driver.find_element_by_id("InfoReq1_lnkElectrical").click()	
	driver.find_element_by_id("InfoReq1_btnEidShowAll").click()	
	soup = BeautifulSoup(driver.page_source, "lxml")
	table = soup.find_all("tr")
	parsed_dict = {}
	
	for row in table:
		data = [cell.string for cell in row]
		if isinstance(data[1], NavigableString) and data[1].startswith("EW"):
			temp_dict = {
				"block" : data[2],
				"lot" : data[3],
				"street_number" : data[4],
				"street_name" : data[5],
				"unit" : data[6],
				"current_stage" : data[7],
				"stage_date" : data[8]
			}
			parsed_dict[data[1]] = temp_dict
	driver.close()

	# try:
	# 	driver.close()
	# except AttributeError:
	# 	pass

	print json.dumps(parsed_dict, indent=4, separators=(',', ':'))





