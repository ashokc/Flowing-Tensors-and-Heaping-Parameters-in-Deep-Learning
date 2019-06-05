from keras.models import Sequential
from keras.layers import Embedding

nWords = 1024
sequence_length = 25
model = Sequential()
model.add(Embedding(input_dim=nWords, output_dim=256, input_length=sequence_length, name='Embedding_Layer'))

from keras.utils import plot_model
model.summary()
plot_model(model, show_shapes=True, to_file='embed_1.png')
import sys
sys.exit(0)

