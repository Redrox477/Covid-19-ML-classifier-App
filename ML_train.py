import pandas as pd
import pickle
import numpy as np
  
df = pd.read_csv('Covid Data.csv')
df.drop(['USMER','MEDICAL_UNIT','DATE_DIED','ICU'],axis = 1, inplace = True)
# df['Species']= df['Species'].map({'Iris-setosa':0, 'Iris-versicolor':1, 'Iris-virginica':2})
  
X = df.iloc[:,: -1]
y = df.iloc[:,-1]
  
# splitting data into training and testing data with 30 % of data as testing data respectively
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1,  random_state = 0)
  
# importing the random forest classifier model and training it on the dataset
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier()
classifier.fit(X_train, y_train)

# predicting on the test dataset
y_pred = classifier.predict(X_test)
  
# finding out the accuracy
from sklearn.metrics import accuracy_score
score = accuracy_score(y_test, y_pred)  
print(df.head(),score)

pickle_out = open("classifier.pkl", "wb")
pickle.dump(classifier, pickle_out)
pickle_out.close()