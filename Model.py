from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle
import pandas as pd
import numpy as np


x_data  = pd.read_csv("x_data")
y_data = pd.read_csv("y_data")


# dropping unnamed feature
x_data = x_data.drop("Unnamed: 0",axis=1)
y_data= y_data.drop("Unnamed: 0",axis=1)

x_train,x_test,y_train,y_test = train_test_split(x_data,y_data,random_state=1,test_size=0.2)

file_name = "finalized_model.sav"
model = pickle.load(open(file_name,"rb"))

#print(x_data.columns)
#print(y_data.columns)
#print(y_train.shape)
#print(y_data.shape)
#print(x_data.shape)
#print(x_train.shape)

y_train_pred = model.predict(x_train)
y_test_pred = model.predict(x_test)


# print(accuracy_score(y_train,y_train_pred))
# print(accuracy_score(y_test,y_test_pred))
