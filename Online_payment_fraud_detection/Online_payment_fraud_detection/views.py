from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
import pandas as pd
import joblib
models=joblib.load('Trained_model.save')
def homepage(request):
	try:
		if request.method == "GET":
			step = request.GET.get('step')    
			txn  = request.GET.get('transaction')
			amt  = float(request.GET.get('amount'))
			cid = request.GET.get('Customerid')
			rid = request.GET.get('Recipientid')
			nb = float(request.GET.get('New Balance'))
			ob = float(request.GET.get('Old Balance'))
			rnb = float(request.GET.get('Recipient New Balance'))
			rob = float(request.GET.get('Recipient Old Balance'))
			cash_out=debit=payment=transfer=0
			if txn=='CASH_OUT':
				cash_out=1
			elif txn=='CASH_IN':
				debit=1
			elif txn=='PAYMENT':
				payment=1
			else:
				transfer=1
			prediction=[]
			test = pd.DataFrame(data=[[step,amt,ob,nb,rob,rnb,cash_out,debit,payment,transfer]],columns=['step', 'amount', 'oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest','newbalanceDest', 'CASH_OUT', 'DEBIT', 'PAYMENT', 'TRANSFER'])
			prediction.append(models[0].predict(test))
			prediction.append(models[2].predict(test))
			prediction.append(models[3].predict(test))
			if prediction.count(0)>prediction.count(1):
				print("NoFraud")
				pred = "not fraud"
			else:
				print("Fraud")
				pred = "Fraud"
			data={
				'output':pred,
				'step':step,
				'amt':amt,
				'nb':nb,
				'ob':ob,
				'rnb':rnb,
				'rob':rob,
				'cid':cid,
				'rid':rid
			}
			return render(request,"home.html",data)
	except:
		pass 
	return render(request,"home.html")

def indexpage(request):
	return render(request,"index.html")

def aboutuspage(request):
	return render(request,"aboutus.html")

def hiwpage(request):
	return render(request,"hiw.html")