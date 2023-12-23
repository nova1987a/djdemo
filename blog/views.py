from django.shortcuts import render
from django.views import generic
from .models import Blog


# Create your views here.
class BlogList(generic.ListView):
    queryset = Blog.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

    
class BlogDetail(generic.DetailView):
    model = Blog
    template_name = 'blog_detail.html'


def get_random(request):
	luckynum = gather_nums()
	# Pass the imported dict to the templatehttps://github.com/nova1987a
	return  render(request, 'lottery.html', {'r': luckynum})


## New web scraping method , read a single file and generate random numbers
import json

## Open the record file
def gather_nums():
	input_file = '/home/w9saka5ulbu0/public_html/djdemo/blog/frequent_nums.dat'
	with open(input_file, "r") as f:
		data = f.read()
		nums = json.loads(data)

	select_lst = []
	select_lst.append(nums[0])
	## Select if diff of 2 number is equal or larger than 4
	for i in range(len(nums)):
		if nums[i]-select_lst[len(select_lst)-1] >= 4:
			select_lst.append(nums[i])

	random_lst = []
	for j in range(len(select_lst)-1):
		random_num = randrange(select_lst[j], select_lst[j+1])
		random_lst.append(random_num)
	
	final_dict = {"Most frequent number(s)":[], "Lucky number(s)":[]}
	final_dict.update({"Most frequent number(s)":select_lst, "Lucky number(s)":random_lst})
	return final_dict
