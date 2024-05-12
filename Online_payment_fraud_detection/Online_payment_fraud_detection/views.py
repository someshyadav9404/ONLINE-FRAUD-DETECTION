from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
import pandas as pd
import joblib
models=joblib.load('Trained_model.save')
def homepage(request):
	try:
		if request.method == "get":
			step = request.GET.get('step')    
			txn  = request.GET.get('transaction')
			amt  = int(request.GET.get('amount'))
			nb = int(request.GET.get('New Balance'))
			ob = int(request.GET.get('Old Balance'))
			rnb = int(request.GET.get('Recipient New Balance'))
			rob = int(request.GET.get('Recipient Old Balance'))
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
			test=pd.DataFrame(data=[[step,amt,ob,nb,rob,rnb,cash_out,debit,payment,transfer]],columns=['step', 'amount', 'oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest',
       'newbalanceDest', 'CASH_OUT', 'DEBIT', 'PAYMENT', 'TRANSFER'])
			for i in range(len(models)):
				prediction.append(models[i].predict(test))
			if prediction.count(0)>prediction.count(1):
				print("NoFraud")
			else:
				print("Fraud")
	except:
		pass 
	return render(request,"home.html")
