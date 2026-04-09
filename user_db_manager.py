import json
import datetime


def add_character_archetype_prediction_to_user_db(user_id: str, user_first_name: str, user_last_name: str, character_description: str, predicted_archetype_index: int, predicted_archetype_label: str, matching_confidence: float):
    try:
        with open('db/user_db.json', 'r') as file:
            data = json.load(file)

        user_already_in_db = False

        db_operation_feedback = {}

        for user in data["users"]:
            if user["user_id"] == user_id:
                user_already_in_db = True
                user["user_first_name"] = user_first_name
                user["user_last_name"] = user_last_name
                user["last_updated"] = datetime.datetime.now().isoformat()
                user["character_description"] = character_description
                user["matched_archetype_index"] = predicted_archetype_index
                user["matched_archetype_label"] = predicted_archetype_label
                user["matching_confidence"] = matching_confidence
                print("Feedback: The user was already in the database but the records have been updated with the current character archetype matching.")
                db_operation_feedback = {"feedback": "The user was already in the database but the records have been updated with the current character archetype matching."}
                break

        if not user_already_in_db:
            data["users"].append({"user_id": user_id,
                                  "user_first_name": user_first_name,
                                  "user_last_name": user_last_name,
                                  "last_updated": datetime.datetime.now().isoformat(),
                                  "character_description": character_description,
                                  "matched_archetype_index": predicted_archetype_index,
                                  "matched_archetype_label": predicted_archetype_label,
                                  "matching_confidence": matching_confidence})
            print("Success: The new user and their archetype matching have been added to the database.")
            db_operation_feedback = {"feedback": "The new user and their archetype matching have been added to the database."}

        with open('db/user_db.json', 'w') as file:
            json.dump(data, file, indent=1)

        return db_operation_feedback

    except FileNotFoundError:
        print("Error: User database file not found")
        return {"error": "User database file not found"}

    except json.JSONDecodeError:
        print("Error: Invalid JSON format")
        return {"error": "Invalid JSON format"}


def retrieve_user_data_product(user_id: str):
    try:
        with open('db/user_db.json', 'r') as file:
            data = json.load(file)

        for user in data["users"]:
            if user["user_id"] == user_id:
                return user

        return {"error": "User not found"}

    except FileNotFoundError:
        return {"error": "Database file not found"}
    except json.JSONDecodeError:
        return {"error": "Invalid JSON format"}


def retrieve_entire_user_database():
    try:
        with open('db/user_db.json', 'r') as file:
            data = json.load(file)

        return data

    except FileNotFoundError:
        return {"error": "Database file not found"}
    except json.JSONDecodeError:
        return {"error": "Invalid JSON format"}
