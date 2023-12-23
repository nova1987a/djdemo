###---       Web scraping area      ---###
import requests
from bs4 import BeautifulSoup as bs
import re
from random import randrange
from datetime import datetime
from fake_useragent import UserAgent


def lottery_list():
	## Define the URL
	url = "https://www.taiwanlottery.com.tw/lotto/lotto649/history.aspx"
	## import fake user agent with random mode, idea from https://weikaiwei.com/python/python-crawler-fake-useragent/
	ua = UserAgent()
	user_agent = ua.random
	## invoke into the header
	header_user = {'user-agent': user_agent}
	req = requests.get(url, headers=header_user)
	soup = bs(req.text, "lxml")
	lott_dict = {}
	for j in range(10):
		#Create empty list and reg expression for special lottery number
		lott_lst = []
		str2 = f'Lotto649Control_history_dlQuery_SNo_{j}'
		special_num = int(soup.find('span', {'id': re.compile(str2)}).get_text())
		for i in range(1,7):
		# Create reg expression for lottery number
			str1 = f'Lotto649Control_history_dlQuery_No{i}_{j}'
	        	#print(str)
		        # grouping the lottery numbers and strip unnecessary id tags
			lott_num = int(soup.find('span', {'id':re.compile(str1)}).get_text())
		#print(lott_num)
			lott_lst.append(lott_num)
		lott_lst.append(special_num)
		#print(lott_lst)
		## Add new key/item into a dict
		new_mark = {j: lott_lst}
		lott_dict.update(new_mark)
		## Create a new list to calculate numbers appearing count
		new_lst = [0]*50
		for lst in lott_dict.values():
			for i in range(50):
				for j in lst:    
					#print('The count of ',i,' is: ', lst.count(i+1))
					if j == i+1 :   ## if found the number is repeating
                            		## Count
						new_lst[i] = new_lst[i]+1
		## Create a new list for storing number appears over 2 times
		threetime_lst = []
		for k in range(len(new_lst)):
			### if the number repeating more than 3 times
			if new_lst[k] > 3:
				threetime_lst.append(k+1)

	with open("frequent_nums.dat", "w") as fdict:
		fdict.write(str(threetime_lst))
		fdict.close()


if __name__ == '__main__':
	lottery_list()
	print(gather_nums())
	print('Finish web scraping')

