import numpy as np
import Utils as ut
from keras.models import Sequential
from keras.layers import Dense, Dropout

x_train = ut.get_X_train_data()
y_train= ut.get_Y_train_data()
x_test = ut.Train_Data()
model = Sequential()
model.add(Dense(13, input_dim=12, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(13, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

model.fit(x_train, y_train,
          epochs=20,
          batch_size=128)

y_test =model.predict(x_test, batch_size=128, verbose=0)
y_test=ut.ConvertToBynary(y_test)
score = model.evaluate(x_test, y_test, batch_size=128)
print(score)