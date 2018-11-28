import requests
import _pickle as pickle
from ..config import tokenizer_path, serving_url

from keras.preprocessing import sequence


def get_predictions(data):
    with open(tokenizer_path, 'rb') as f:
        tokenizer = pickle.load(f)

    data = data['data']
    sequences = tokenizer.texts_to_sequences(data)
    sequences = sequence.pad_sequences(sequences, maxlen=100)

    instances = []
    for s in sequences:
        instances.append({"sequence": s.tolist()})

    payload = {
        "instances": instances
    }

    print(payload)

    predictions = requests.post(f"http://{serving_url}/v1/models/senticloud:predict", json=payload).json()
    flattened = [p[0] for p in predictions["predictions"]]

    return {'predictions': flattened}