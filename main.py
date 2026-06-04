from modules.loader import load_knowledge
from modules.embedder import create_embeddings
from modules.similarity import calculate_similarity
from modules.retriever import retrieve_answer

knowledge = load_knowledge("documents/knowledge.txt")

embeddings, model = create_embeddings(knowledge)

print("\nChat with TXT File")
print("Type 'exit' to quit\n")

while True:

    query = input("You: ")

    if query.lower() == 'exit':
        break

    query_embedding = model.encode(query)

    scores = calculate_similarity(query_embedding, embeddings)

    answer = retrieve_answer(knowledge, scores)

    print(f"\nBot: {answer}\n")