from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.views.generic import TemplateView
import json
from interviews.models import Answers, MetaData

def index(request):
	return render(request, 'interviews/base.html') 


def interviews(request):
	meta_data = MetaData.objects.values().order_by('id')
	answers = Answers.objects.values()

	foo = {

	}

	for i in meta_data:
		foo[i["interview_id"]] = i
		for answer in answers:
		    if i["interview_id"] == answer["interview_id"] :
		        foo[i["interview_id"]][str(answer["section_number"])+"_"+str(answer["sub_section_number"])+"_"+str(answer["answer_number"])+"_"+str(answer["question_number"])] = answer["answer"]

	dataq = json.dumps(foo)
	return render(request, 'interviews/interviews.html', {'data': dataq, 'k' :True }) 

def baa(request):
	meta_data = MetaData.objects.values().order_by('id')[:40]
    #foo = {'data':meta_data}
	meta__ = []
	baa = voo("4YTO7B74",1,0,1,1)
	keys = range(len(meta_data))
	answers__ = { }
	foo = {

	}
	for i in meta_data:
		foo[i["interview_id"]] = i

		#SECTION ONE
		if  voo(i["interview_id"] , 1,0,1,1)  != "empty" :
			foo[i["interview_id"]]["s_1_0_1_1"] = voo(i["interview_id"], 1,0,1,1)
		if voo(i["interview_id"] , 1,0,1,2)  != "empty" : 
			foo[i["interview_id"]]["s_1_0_1_2"] = voo(i["interview_id"], 1,0,1,2)

		if voo(i["interview_id"] , 1,0,1,3)  != "empty" : 
			foo[i["interview_id"]]["s_1_0_1_3"] = voo(i["interview_id"], 1,0,1,3)
		if voo(i["interview_id"] , 1,0,1,4)  != "empty" : 
			foo[i["interview_id"]]["s_1_0_1_4"] = voo(i["interview_id"], 1,0,1,4)
		if voo(i["interview_id"] , 1,0,1,5)  != "empty" : 
			foo[i["interview_id"]]["s_1_0_1_5"] = voo(i["interview_id"], 1,0,1,5)			


	dataq = json.dumps(foo)
	return render( request, 'interviews/test.html', {'data': dataq} )
