import numpy as np


def softmax(values):

    values = np.array(values)

    values = values - np.max(values)

    exp_values = np.exp(values)

    return exp_values / np.sum(exp_values)


def calculate_attention(embeddings):

    if len(embeddings) == 0:
        return []

    # Query
    query = np.mean(
        embeddings,
        axis=0
    )

    # Attention score for each word
    scores = []

    for embedding in embeddings:

        score = np.dot(
            embedding,
            query
        )

        scores.append(score)

    # Convert scores into probabilities
    attention_scores = softmax(scores)

    return attention_scores.tolist()
