import os
import re
import sys

# First open the LOG for to ana



def search_go(filename):
	fd = open (filename,'r')
	lines = fd.readlines()
	for index ,line in enumerate(lines):
		newLine = line.rstrip()
		newLine = 'Line'+'->'+str(index+1)+':'+newLine
		lines[index] = newLine
	# Fromat this LOG data if its have line u can ignore for_loop！
	# we can use readlines() but its can give us corrects lines number 
	# push_back the log in a list to use list to ana LOG 

	#defind some list and vars



	Key_word_1 = 'C2-AsiRp1Agentexe INF/OAM/AsiHubDiscoveryObserver.cpp:77:handle(): ['
	Key_word_2 = 'C2-AsiRp1Agentexe DBG/OAM/AsiHubDiscoveryObserver.cpp:178:findMatchedHubmod(): ['
	Key_word_3 = 'C2-AsiRp1Agentexe INF/OAM/AsiHubDiscoveryObserver.cpp:147:getMatchedHubmodR(): ['
	Key_word_4 = 'C2-AsiRp1Agentexe INF/OAM/AsiHubDiscoveryObserver.cpp:217:fillHubmodR(): ['
	Key_word_5 = 'C2-AsiRp1Agentexe INF/OAM/AsiHubDiscoveryObserver.cpp:93:handle(): ['



	# get thr first key word line and index
	# must defind global var or Error for the pro
	# ii can get Loop times 
	global ii
	ii = 0
	#can get the lines index
	global Save_list_UP
	Save_list_UP = []
	# save the keyword1_ list to using show
	global search_one_line_list
	search_one_line_list = []
	
	
	
	
	
	# we defined a var to get the first key word times
	for search_one_line in lines:
		if Key_word_1 in search_one_line:
			# we know the line's 
			search_one_line_list.append(search_one_line)
			# we know the line's index                         
			Save_list_UP.append(lines.index(search_one_line))
			# we know the discover times 
			ii += 1
###################################Back Search Only one Line################################################################

	def back_search_to_find_Title():
		global Save_list_back_line_demo
		Save_list_back_line_demo = []
		global Save_list_back_line
		Save_list_back_line = []
		num_title = 0
		# this is regular to search sth. in syslog
		regex = re.compile(r'Line->(?P<line>\d{1,7}):'+
					r'.*(?P<date><\d.*?\w>)'+
					r'.*<from>(?P<from>.*?)</from>'+
					r'<id>(?P<id>\d{1,5})</id>'+
					r'<relatesTo>(?P<port>.*?[^\s])</relatesTo>'+
					r'<to>(?P<to>.*?)</to>')
		while num_title < ii :
			if num_title == 0 and num_title < ii:
				for search_back_line_list in lines[0:Save_list_UP[num_title]]:
					m = regex.search(search_back_line_list)
					if not m :
						continue
					# push the result in a test or file 
					search_back_line_list = 'line : %s,date :%s,form: %s,id: %s,realseto: %s ,to: %s '%(m.group('line'),
						m.group('date'),
						m.group('from'),
						m.group('id'),
						m.group('port'),
						m.group('to')
						)
					Save_list_back_line_demo.append(search_back_line_list)
				Save_list_back_line.append(Save_list_back_line_demo[-1])
				num_title +=1
			elif num_title != 0 and num_title < ii :
				for search_back_line_list in lines[Save_list_UP[num_title-1]:Save_list_UP[num_title]]:
					m = regex.search(search_back_line_list)
					if not m :
						continue
					search_back_line_list = 'line : %s,date :%s,form: %s,id: %s,realseto: %s ,to: %s ' %(m.group('line'),
						m.group('date'),
						m.group('from'),
						m.group('id'),
						m.group('port'),
						m.group('to')
						)
					Save_list_back_line_demo.append(search_back_line_list)
				Save_list_back_line.append(Save_list_back_line_demo[-1])
				num_title +=1
###################################Back Search Only one Line################################################################
	
	def search_two():
		# two_log_keyword
		global search_two_line_list 
		search_two_line_list = []
		num_title = 0
		while num_title < ii :
			if num_title < 4 and num_title < ii :
				for search_two_list in lines[Save_list_UP[num_title]:Save_list_UP[num_title+1]]:
					if Key_word_2 in search_two_list :
						search_two_line_list.append(search_two_list)
				num_title +=1
			if num_title == 4 :
				for search_two_list in lines[Save_list_UP[num_title]:]:
					if Key_word_2 in search_two_list:
						search_two_line_list.append(search_two_list)
				num_title +=1
	# go the next step
	back_search_to_find_Title()
	search_two()
	

# aaa = re.compile(r'C2-AsiRp1Agentexe .*?findMatchedHubmod')
# for line in lines:
# 	aa = aaa.search(line)
# 	if not aa :
# 		continue
# 	print (line)
def write_ana_log():
	print (search_two_line_list)
	print (search_one_line_list)
	print (Save_list_back_line)
