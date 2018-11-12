import requests
import _pickle as pickle
from ..config import paths, endpoints

from keras_preprocessing import sequence


def get_predictions(data):

    with open(paths['tokenizer'], 'rb') as f:
        tokenizer = pickle.load(f)

    sequences = tokenizer.texts_to_sequences(data)
    sequences = sequence.pad_sequences(sequences)

    return requests.post(endpoints['serving'], sequences)
