from text_embedding import embed_character_description

def predict_character_archetype(input_character_description):
    embedded_character_description = embed_character_description(input_character_description)
    print(embedded_character_description)
    return embedded_character_description