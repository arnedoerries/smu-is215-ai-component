import pandas as pd
from sentence_transformers import SentenceTransformer
import numpy as np

# Loading the SBERT embedding model with 384 dimensions
model = SentenceTransformer("all-MiniLM-L6-v2")


def embed_labeled_training_data(input_character_description_df: pd.DataFrame):
    # Embedding each character description from the input
    X = embedded_character_descriptions = model.encode(
        input_character_description_df['character_description'].tolist(),
        convert_to_numpy=True,
        show_progress_bar=True,
        normalize_embeddings = True
    )

    # Just taking over the label as it is already encoded
    y = np.array(input_character_description_df['label'].tolist())

    # Returning the two lists for X (embedded character descriptions) and y (corresponding labels)
    return X, y


# Embedding the raw user input description
def embed_character_description(input_character_description: str):
    embedded_character_description = model.encode(
        [input_character_description],
        convert_to_numpy=True,
        normalize_embeddings=True
    )
    print("The character description has been embedded:")
    print(embedded_character_description)
    return embedded_character_description