from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def semantic_similarity(text1, text2):
    """
    Compute semantic similarity using TF-IDF.
    Returns a value between 0 and 1.
    """

    vectorizer = TfidfVectorizer(stop_words="english")

    vectors = vectorizer.fit_transform([text1, text2])

    similarity = cosine_similarity(
        vectors[0],
        vectors[1]
    )[0][0]

    return float(similarity)