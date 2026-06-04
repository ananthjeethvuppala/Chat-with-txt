def load_knowledge(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
    chunks = text.split("\n\n")

    return [chunk.strip() for chunk in chunks if chunk.strip()]