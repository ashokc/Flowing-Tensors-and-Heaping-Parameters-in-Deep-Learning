from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.layers import Embedding
from keras.layers import LSTM, GRU

nWords = 1000
sequence_length = 25
model = Sequential()
model.add(Embedding(input_dim=nWords, output_dim=256, input_length=sequence_length, name='Embedding_Layer'))
model.add(GRU(128,name='GRU_Layer'))
model.summary()

from keras.utils import plot_model
plot_model(model, show_shapes=True, to_file='gru.png')
import sys
sys.exit(0)
