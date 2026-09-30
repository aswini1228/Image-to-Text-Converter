import numpy as np


def create_embeddings(words):

    embeddings = []

    for word in words:

        vector = np.array([
            len(word),
            sum(ord(char) for char in word) % 100,
            sum(char.isupper() for char in word),
            sum(char.islower() for char in word),
            sum(char.isdigit() for char in word)
        ], dtype=float)

        norm = np.linalg.norm(vector)

        if norm != 0:
            vector = vector / norm

        embeddings.append(vector)

    return np.array(embeddings)
