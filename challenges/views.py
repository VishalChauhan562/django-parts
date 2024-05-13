from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse


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

def index(request):
    try:
        month_list = list(definitions.keys())
        return render(request,"challenges/index.html",{
                "month_list" : month_list
            })
    except:
        raise Http404()  

def monthly_challenge_name(request,month):
    try:
        month_text = definitions[month]
        return render(request,"challenges/challenge.html",{
            "month_text" : month_text,
            "month" : month
        })
    except:
        raise Http404()  

def monthly_challenge_number(request,month):
    try:
        month_keys = list(definitions.keys())
        month_came = month_keys[month - 1]
        redirect_path = reverse('month-challenge',args=[month_came])
        return HttpResponseRedirect(redirect_path)
    except:
        raise Http404()  