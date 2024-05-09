from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect


def homepage(request):
    try:
        txn = request.GET.get('transaction')
        amt = int(request.GET.get('amount'))
        cid = request.GET.get('cid')
        rid = request.GET.get('rid')
        nb = int(request.GET.get('New Balance'))
        ob = int(request.GET.get('Old Balance'))
        rnb = int(request.GET.get('Recipient New Balance'))
        rob = int(request.GET.get('Recipient Old Balance'))
    except:
        pass 
    return render(request,"home.html")
