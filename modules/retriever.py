def retrieve_answer(chunks, similarity_scores, threshold=0.35):
    best_match_index = (similarity_scores.argmax())
    best_score = similarity_scores[best_match_index]

    if best_score < threshold:
        return (
            "Sorry, I could not "
            "find relevant information."
        )
    
    return chunks[best_match_index]