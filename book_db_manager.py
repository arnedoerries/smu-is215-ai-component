import datetime
import json


def add_new_book_character_to_book_db(book_id: str, book_title: str, book_published_date: datetime.date, book_genre: str, book_summary: str, character_name: str, character_gender: str, character_description: str, matched_archetype_id: int, matched_archetype_label: str, matching_confidence: float):
    try:
        with open('db/book_db.json', 'r') as file:
            data = json.load(file)

        book_already_in_db = False
        character_already_in_db = False

        db_operation_feedback = {}

        for book in data["books"]:
            if book["book_id"] == book_id:
                book_already_in_db = True
                for character in book["main_characters"]:
                    if character["name"] == character_name:
                        character_already_in_db = True

                        print("Feedback: This book and character are already documented in the book database")
                        db_operation_feedback = {"feedback": "This book and character are already documented in the book database"}

                        break

                if not character_already_in_db:
                    book["main_characters"].append({
                        "name": character_name,
                        "gender": character_gender,
                        "description": character_description,
                        "archetype_id": matched_archetype_id,
                        "archetype_label": matched_archetype_label,
                        "confidence": matching_confidence
                    })

                    print("Success: The book already exists in the database, but the new character has been successfully added.")
                    db_operation_feedback = {"success" : "The book already exists in the database, but the new character has been successfully added."}

                break

        if not book_already_in_db:
            data["books"].append({"book_id": book_id,
                                  "title": book_title,
                                  "published_date": book_published_date.isoformat(),
                                  "genre": book_genre,
                                  "summary": book_summary,
                                  "main_characters": [{
                                      "name": character_name,
                                      "gender": character_gender,
                                      "description": character_description,
                                      "archetype_id": matched_archetype_id,
                                      "archetype_label": matched_archetype_label,
                                      "confidence": matching_confidence
                                  }]
                                  }
                                 )
            print("Success: The new book and new character have been successfully added to the book database.")
            db_operation_feedback = {"success": "The new book and new character have been successfully added to the book database."}

        matching_results = {
            "character_name": character_name,
            "matched_archetype": matched_archetype_label,
            "matching_confidence": matching_confidence,
        }

        return_message = {
        "matching_results": matching_results,
        "db_operation_feedback": db_operation_feedback
        }

        with open('db/book_db.json', 'w') as file:
            json.dump(data, file, indent=1)

        return return_message

    except FileNotFoundError:
        print("Error: Book database file not found")
        return {"error": "Book database file not found"}
    except json.JSONDecodeError:
        return {"error": "Invalid JSON format"}


def retrieve_book_data_product(book_id: str):
    try:
        with open('db/book_db.json', 'r') as file:
            data = json.load(file)

        for book in data["books"]:
            if book["book_id"] == book_id:
                return book

        return {"error": "Book not found"}

    except FileNotFoundError:
        return {"error": "Book database file not found"}
    except json.JSONDecodeError:
        return {"error": "Invalid JSON format"}


def retrieve_entire_book_database():
    try:
        with open('db/book_db.json', 'r') as file:
            data = json.load(file)

        return data

    except FileNotFoundError:
        return {"error": "Book database file not found"}
    except json.JSONDecodeError:
        return {"error": "Invalid JSON format"}


def recommend_books_based_on_archetype(archetype_id: int):
    try:

        recommended_books = []

        with open('db/book_db.json', 'r') as file:
            data = json.load(file)

        for book in data["books"]:
            matching_characters = []

            for character in book["main_characters"]:
                if character["archetype_id"] == archetype_id:
                    matching_characters.append(character)

            if matching_characters:
                recommended_books.append({
                    "title": book["title"],
                    "published_date": book["published_date"],
                    "genre": book["genre"],
                    "summary": book["summary"],
                    "matching_characters": matching_characters
                })

        recommended_books.sort(key=lambda added_book : added_book["published_date"], reverse=True)

        recommended_books_and_characters = {"recommended_books" : recommended_books}
        return recommended_books_and_characters

    except FileNotFoundError:
        return {"error": "Database file not found"}
    except json.JSONDecodeError:
        return {"error": "Invalid JSON format"}
