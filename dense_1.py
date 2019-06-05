
from keras.models import Sequential
from keras.layers import Dense, Activation

# this is preferred because it leads to a smaller picture from plot_model. And we asoociate activation function directly when defining a layer... 

model = Sequential()
model.add(Dense(units=32, input_shape=(784,), name='Dense_Layer'))

from keras.utils import plot_model
model.summary()
plot_model(model, show_shapes=True, to_file='dense_1.png')
import sys
sys.exit(0)

