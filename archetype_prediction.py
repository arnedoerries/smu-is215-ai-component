from tensorflow import keras
import numpy as np

from text_embedding import embed_character_description


ARCHETYPE_LABELS = {
    0: "The Quiet Thinker",
    1: "The Bold Leader",
    2: "The Caring Heart",
    3: "The Free Spirit",
}


classifier = keras.models.load_model("model.keras")


def predict_character_archetype(character_description: str):
    embedded_character_description = embed_character_description(character_description)

    # Run the embedding through the Keras classifier
    probabilities = classifier.predict(embedded_character_description, verbose=0)

    # Get the predicted class index and confidence score
    matched_archetype_index = int(np.argmax(probabilities[0]))
    matched_archetype_label = ARCHETYPE_LABELS[matched_archetype_index]
    matching_confidence = round(float(np.max(probabilities[0])), 2)

    return matched_archetype_index, matched_archetype_label, matching_confidence