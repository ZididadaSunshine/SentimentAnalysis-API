import requests
import _pickle as pickle
from ..config import tokenizer_path, serving_url

from keras.preprocessing import sequence


def get_predictions(data):

    with open(tokenizer_path, 'rb') as f:
        tokenizer = pickle.load(f)

    sequences = tokenizer.texts_to_sequences(data)
    sequences = sequence.pad_sequences(sequences)

    return requests.post(serving_url, sequences)
