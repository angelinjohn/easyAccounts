import os
# mathematical computation
import numpy as np
# manipulate csv
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

from sklearn.model_selection import train_test_split
# recursive feature elimination for 
from sklearn.feature_selection import RFE
df_tax_data = pd.read_csv('tax_data.csv')
#One hot encoding of Y-values
y= df_tax_data['STATE_x']
label_encoder = LabelEncoder()
integer_encoded = label_encoder.fit_transform(y)
# print('Label encoded value',integer_encoded)
onehot_encoder = OneHotEncoder(sparse=False)
integer_encoded = integer_encoded.reshape(-1, 1)

onehot_encoded = onehot_encoder.fit_transform(integer_encoded)
print('One hot encoded', onehot_encoded)
df_train_x = df_tax_data.drop(["STATE_x"],1) 
df_train_y = onehot_encoded

X_train, X_test, y_train, y_test = train_test_split(df_train_x, df_train_y, test_size=0.2)
print('Train shape', X_train.shape)
print('Test shape', X_test.shape)

print('Output', y_test.shape )

from keras import Sequential
from keras.layers import Dense

model = Sequential()
# The Input Layer :
model.add(Dense(128, input_dim = X_train.shape[1], activation='relu'))

# The Hidden Layers :
model.add(Dense(256, activation='relu'))
model.add(Dense(256, activation='relu'))
#     model.add(Dense(256, kernel_initializer='normal',activation='relu'))

# The Output Layer :
model.add(Dense(51, activation='softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy')
model.summary()

model.fit(X_train, y_train, epochs=10)

y_pred= model.predict(X_test)
print(y_pred)
y_pred.shape
y_test.shape

pickle.dump(model, open('model.pkl','wb'))
