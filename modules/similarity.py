from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(query_embeddings, knowledge_embeddings):
    similarity_score = cosine_similarity([query_embeddings], knowledge_embeddings)

    return similarity_score[0]