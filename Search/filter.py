# Developed and modified by Ye Liang at 15:16 Oct,25 2015
# All rights reserved
import re
#---------context--http-----------------------------
pattern_1 = "(.*?)http(.*?)$"
#---------RT @SportsCenter:context------------------
pattern_2 = "RT\s@(.*?):\s(.*?)$"
#---------@austin_brown051 context------------------
pattern_3 = "@(.*?)\s(.*?)$"

#---------filters assembly--------------------------
filter_1 = re.compile(pattern_1,re.IGNORECASE)
filter_2 = re.compile(pattern_2,re.IGNORECASE)
filter_3 = re.compile(pattern_3,re.IGNORECASE)

class Search_Result:
	def __init__(self, text, url):
		self.text = text
		self.url = url

def IsValidInformation(content):
	if(len(content) > 5):

#-----------add prerequisits here------------------------------------------------------
		return True
	else: 
		return False

def TwitterFilter(twi_result):
	filtered_result_list = []
	for result in twi_result:
		result = result.decode('utf-8','ignore')
#--------------split url and content----------------------------------------------------
		case_1 = re.match(filter_1, result)#text for group(1), url for group(2)
		if (case_1):
			result_text = case_1.group(1)
			result_url = 'http' + case_1.group(2)
		else:
			result_text = result
			result_url = "empty"
#-------------remove RT @Sb:------------------------------------------------------------
		case_2 = re.match(filter_2, result_text)#group(2)
		if (case_2):
			result_text = case_2.group(2)
#-------------remove @Sb:---------------------------------------------------------------
		case_3 = re.match(filter_3, result_text)#group(2)
		if (case_3):
			result_text = case_3.group(2)
#-------------remove too shrot content--------------------------------------------------
		if(IsValidInformation(result_text)):
			filtered_result = Search_Result(result_text, result_url)
			filtered_result_list.append(filtered_result)
	return filtered_result_list