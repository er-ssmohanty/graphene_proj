import pandas as pd
import numpy as np
from sklearn import svm
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

grd = pd.read_csv("graphene_data_final.csv")

X = grd[['Graphene_percentage', 'FEED', 'RPM', 'DOC']]  
Y = grd['MRR_gm_per_sec']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.3, random_state=1)

model = svm.SVR()
model.fit(X_train, Y_train)

print(model.score(X_test,Y_test))
