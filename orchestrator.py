import datetime

from archetype_prediction import predict_character_archetype
from user_db_manager import add_character_archetype_prediction_to_user_db
from book_db_manager import add_new_book_character_to_book_db, recommend_books_based_on_archetype

def predict_for_user_and_add_to_user_db(user_id: str, user_first_name: str, user_last_name: str, character_description: str):

    matched_archetype_index, matched_archetype_label, matching_confidence = predict_character_archetype(character_description)

    if matching_confidence < 0.8:
        return {
            "user feedback": "Sorry, we couldn't match your description to any character archetype. Please select one manually.",
            "system feedback": "Nothing has been added to or changed about the user database."
        }

    add_character_archetype_prediction_to_user_db(user_id, user_first_name, user_last_name, character_description, matched_archetype_index, matched_archetype_label, matching_confidence)

    summary = {
        "archetype": matched_archetype_label,
        "confidence": matching_confidence
    }

    return summary

def predict_for_new_character_and_add_to_book_db(book_id: str, book_title: str, book_published_date: datetime.date, book_genre: str, book_short_summary: str, character_name: str, character_gender: str, character_description: str):

    matched_archetype_index, matched_archetype_label, matching_confidence = predict_character_archetype(character_description)

    if matching_confidence < 0.8:
        return {
            "feedback": "The classifier couldn't identify a good character archetype match for this book's character. Nothing hsa been added to the database."
        }

    return add_new_book_character_to_book_db(book_id, book_title, book_published_date, book_genre, book_short_summary, character_name, character_gender, character_description, matched_archetype_index, matched_archetype_label, matching_confidence)



