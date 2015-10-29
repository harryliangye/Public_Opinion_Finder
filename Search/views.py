# Developed and modified by Ye Liang at 16:03 Oct,25 2015
# All rights reserved
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render, render_to_response
from _collections import deque
from .engine import NewResult
from .filter import Search_Result
from .sentiment import SentimentAnalyzer,SentimentAnalyzer1000
#Begin-------------------------------------Server-Initialization------------------------------------Begin#
g_memory_pointer = 0
g_runtime_memory = []

class Search_Scene:
	def __init__(self,usrid):
		self.page = 0
		self.twitter_sid = 1
		self.query = ""
		self.usr_id = usrid
		self.search_results = []

for g_memory_pointer in range(0,100):
	new_scene = Search_Scene(-1)
	g_runtime_memory.append(new_scene)
#End---------------------------------------Server-Initialization--------------------------------------End#
def home_page(request):
	return render(request,'Search/home_page.html')

def find(request):
	if (request.method == 'GET'):
		return_uid = AllocateNewMemory(request.GET['query'])
		(page, search_results, query) = UsrReqPro(return_uid, 0)
	else:
		return_uid = request.session.get('visitor_id')
		if('P' in request.POST):
			action = -1
		else:
			action = 0
		(page, search_results, query) = UsrReqPro(return_uid, action)
	request.session['visitor_id'] = return_uid
	return render(request,'Search/find.html',{'query':query, 'result_list':search_results, 'page':page})

def SentimentView(request):
	if (request.method == "POST"):
		return_uid = request.session.get('visitor_id')
		request.session['visitor_id'] = return_uid
		render_data = SentimentRequestProcess(return_uid)
		return render(request,'Search/SentimentView.html',{'pos':render_data[0],'neu':render_data[1],'neg':render_data[2]})
	else:
		return None

def SentimentRequestProcess(return_uid):
	global g_runtime_memory
	usr = FindUser(return_uid)
	if (len(g_runtime_memory[usr].search_results) < 1000):
		(new_result, g_runtime_memory[usr].twitter_sid) = NewResult(g_runtime_memory[usr].query, 
			g_runtime_memory[usr].twitter_sid, 1000 - len(g_runtime_memory[usr].search_results))
		SentimentAnalyzer(new_result)
		g_runtime_memory[usr].search_results += new_result
	data_set = SentimentAnalyzer1000(g_runtime_memory[usr].search_results)
	return data_set

def UsrReqPro(return_id, action):
	# action == 1 : next, action == 0 : previous
	global g_runtime_memory
	for usr in range(0,100):
		if(return_id == g_runtime_memory[usr].usr_id):#find the user
			if(action == -1):#previous page, no more search here
				g_runtime_memory[usr].page -= 1
			else:
				current_res_count = len(g_runtime_memory[usr].search_results)
				expected_res_count = 20 * (g_runtime_memory[usr].page + 1)
				if(current_res_count < expected_res_count):
					(new_result, g_runtime_memory[usr].twitter_sid) = NewResult(g_runtime_memory[usr].query, 
						g_runtime_memory[usr].twitter_sid, expected_res_count - current_res_count )#if there's a need to search
					#sentiment analysis using natural language processing unit
					SentimentAnalyzer(new_result)
					#----------------------------------------------------end----
					g_runtime_memory[usr].search_results += new_result
				g_runtime_memory[usr].page += 1
#------------------return begins-----------------------begins---------
			return_page = g_runtime_memory[usr].page
			return_q = g_runtime_memory[usr].query
			return_results = g_runtime_memory[usr].search_results[((g_runtime_memory[usr].page - 1)* 20) : 
																		(g_runtime_memory[usr].page * 20)]
			return (return_page, return_results, return_q)	
	return None
def FindUser(uid):
	for usr in range(0,100):
		if(uid == g_runtime_memory[usr].usr_id):
			return usr
	return None
def AllocateNewMemory(query):
	global g_runtime_memory
	global g_memory_pointer
	g_runtime_memory[(g_memory_pointer % 100)].usr_id = g_runtime_memory[((g_memory_pointer - 1) % 100)].usr_id + 100
	g_runtime_memory[(g_memory_pointer % 100)].page = 0
	g_runtime_memory[(g_memory_pointer % 100)].query = query
	g_memory_pointer += 1
	return g_runtime_memory[((g_memory_pointer - 1) % 100)].usr_id