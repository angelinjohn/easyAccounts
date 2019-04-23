import os
# mathematical computation
import numpy as np
# manipulate csv
import pandas as pd
import pickle

# Visualization
import seaborn as sns

from sklearn.model_selection import train_test_split
# recursive feature elimination for 
from sklearn.feature_selection import RFE
tax_data = pd.read_csv('taxDetails.csv')
tax_data.head()
corr= tax_data.corr()
sns.heatmap(corr)

#Correlation with output variable
cor = tax_data.corr()
cor_target = abs(cor["A09400"])
#Selecting highly correlated features
relevant_features = cor_target[cor_target>0.8]
selected_features_list=relevant_features.keys()
filtered_data=tax_data[selected_features_list]
tax=filtered_data["A09400"].values
features=filtered_data.drop("A09400",1) 


from sklearn.preprocessing import  MinMaxScaler
sc= MinMaxScaler()
X= sc.fit_transform(features)
y= tax.reshape(-1,1)
y=sc.fit_transform(y)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
print(X_test.shape[0])
print(X_train.shape[0])

from keras import Sequential
from keras.layers import Dense
def build_regressor():
    regressor = Sequential()
    # The Input Layer :
    regressor.add(Dense(128, kernel_initializer='normal',input_dim = X_train.shape[1], activation='relu'))

    # The Hidden Layers :
    regressor.add(Dense(256, kernel_initializer='normal',activation='relu'))
    regressor.add(Dense(256, kernel_initializer='normal',activation='relu'))
    regressor.add(Dense(256, kernel_initializer='normal',activation='relu'))

    # The Output Layer :
    regressor.add(Dense(1, kernel_initializer='normal',activation='linear'))

    regressor.compile(optimizer='adam', loss='mean_squared_error',  metrics=['mean_absolute_error'])
    return regressor

from keras.wrappers.scikit_learn import KerasRegressor
regressor = KerasRegressor(build_fn=build_regressor, batch_size=32,epochs=10)
build_regressor().summary()

results=regressor.fit(X_train,y_train)

y_pred= regressor.predict(X_test)

pickle.dump(regressor, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[1.8]]))