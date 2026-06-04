def retrieve_answer(chunks, similarity_scores):
    best_match_index = (similarity_scores.argmax())
    return chunks[best_match_index]