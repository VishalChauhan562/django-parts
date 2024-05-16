from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .models import Month
from .serializers import MonthSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Avg




# Create your views here.

definitions = {
    "january": "January is named after Janus, the Roman god of beginnings and transitions.",
    "february": "February is the only month that can pass without a full moon occurring.",
    "march": "March was originally the first month of the Roman calendar.",
    "april": "April's name comes from the Latin word 'aperire', which means 'to open' or 'bloom'.",
    "may": "May's birthstone is the emerald which symbolizes love and success.",
    "june": "June is named after Juno, the Roman goddess of marriage and childbirth.",
    "july": "July was named by the Roman Senate in honor of Julius Caesar.",
    "august": "August was originally named 'Sextilis' in Latin, as it was the sixth month of the Roman calendar.",
    "september": "September comes from the Latin word 'septem', meaning 'seven'.",
    "october": "October's birth flower is the calendula or marigold, which symbolizes sorrow or sympathy.",
    "november": "November is often associated with Movember, an annual event involving the growing of mustaches during the month to raise awareness of men's health issues.",
    "december": None
}

#  FUnctions handeling views
def index(request):
    try:
        month_list = list(definitions.keys())
        month = Month.objects.all().order_by("name")  # use -name for reverse order
        month_count = month.count()
        month_position_avg = month.aggregate(Avg("position")) 
        serialized_months = MonthSerializer(month,many=True)
        print("==========>",serialized_months.data)
        return render(request,"challenges/index.html",{
                "month_list" : serialized_months.data,
                "month_count" : month_count,
                "avg" : month_position_avg
            })
    except Exception as e:
        print("Error in index===>",e)
        raise Http404()  

def monthly_challenge_name(request,id):
    try:
        month_obj = Month.objects.get(pk=id)
        serialized_month = MonthSerializer(month_obj)
        python_data =  serialized_month.data
        # print("====>",serialized_month.data['idea'])
        return render(request,"challenges/challenge.html",{
            "month_data" : python_data
        })
    except Exception as e:
        print("Error in index===>",e)
        raise Http404()    


# Function handeling APIS

def month_detail(request,pk):
    month = Month.objects.get(position=pk)   
    serialized_month = MonthSerializer(month)
    json_data = JSONRenderer().render(serialized_month.data)
    return HttpResponse(json_data,content_type='application/json')
    # same as above two lines 
    # return JsonResponse(serialized_month.data) 


def month_list(request):
    month = Month.objects.all() 
    serialized_month = MonthSerializer(month,many=True)
    json_data = JSONRenderer().render(serialized_month.data)
    return HttpResponse(json_data,content_type='application/json')
    # same as above two lines 
    # return JsonResponse(serialized_month.data,safe=False)
    
@csrf_exempt
def month_create(request):
    if request.method =='POST':
        json_data = request.body 
        stream = io.BytesIO(json_data)     
        python_data = JSONParser().parse(stream)
        serializer = MonthSerializer(data=python_data)
        if(serializer.is_valid()):
            serializer.save()
            res = {"msg":"success"}
            json_res = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')

        err_res = JSONRenderer().render(serializer.errors)
        return HttpResponse(err_res,content_type='application/json')    