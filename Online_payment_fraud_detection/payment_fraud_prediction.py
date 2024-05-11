#importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Reading dataframe
url=('https://raw.githubusercontent.com/someshyadav9404/ONLINE-PAYMNET-FRAUD-DETECTION/main/Online_payment_fraud_detection/online_Fraud_balance.csv')
data=pd.read_csv(url,index_col=0)
data.head()
# Getting sample
data.sample(10)
# checking dataframe
data.shape
# checking missing values
data.isnull().sum()
# checking duplicate
data.duplicated().sum()
# checking datatypes
data.info()
# checking datatypes
obj = (data.dtypes == 'object')
object_cols = list(obj[obj].index)
print("Categorical variables:", len(object_cols))

int_ = (data.dtypes == 'int')
num_cols = list(int_[int_].index)
print("Integer variables:", len(num_cols))

fl = (data.dtypes == 'float')
fl_cols = list(fl[fl].index)
print("Float variables:", len(fl_cols))
# checking for number of values unique in coloumn
data.nunique()
# check statistic of dataset
data.describe()
#checking unipue values
data['type'].value_counts()
data['nameDest'].value_counts()
data['step'].value_counts()
data['isFraud'].value_counts()
# data visualisation
sns.barplot(x='type', y='amount', data=data,hue='isFraud')
sns.countplot(x='type', data=data)
sns.countplot(x='type', data=data,hue='isFraud')
sns.lineplot(data=data, x="amount", y="oldbalanceOrg", hue="type")
#dropping unused columns
data1=data.drop(['type','nameOrig','nameDest'],axis=1)
# correlation
plt.figure(figsize=(12, 6))
sns.heatmap(data1.corr(),cmap='BrBG',fmt='.2f',linewidths=2,annot=True)
# one hot enoding
type_new = pd.get_dummies(data['type'], drop_first=True)
data_new = pd.concat([data, type_new], axis=1)
data_new.head()
# droping irrivalent clumns
X = data_new.drop(['isFraud', 'type', 'nameOrig', 'nameDest'], axis=1)
y = data_new['isFraud']
# checking datashape
X.shape,y.shape
# checking training features
X.columns
#Performing test train spilt
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
X_train.head()
y_train.head()
from xgboost import XGBClassifier
from sklearn.metrics import roc_auc_score as ras
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
#creating model
models = [LogisticRegression(), XGBClassifier(),SVC(kernel='rbf', probability=True),RandomForestClassifier(n_estimators=7,criterion='entropy',random_state=7)]
for i in range(len(models)):
	models[i].fit(X_train, y_train)
	print(f'{models[i]} : ')

	train_preds = models[i].predict_proba(X_train)[:, 1]
	print('Training Accuracy : ', ras(y_train, train_preds))

	y_preds = models[i].predict_proba(X_test)[:, 1]
	print('Validation Accuracy : ', ras(y_test, y_preds))
	print()  
# Saving model 
import pickle
save_model=pickle.dumps(models)

