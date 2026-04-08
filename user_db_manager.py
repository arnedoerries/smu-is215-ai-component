import json
import datetime

def add_character_archetype_prediction_to_user_db(user_id: str, user_first_name: str, user_last_name: str, character_description: str, predicted_archetype_index: int, predicted_archetype_label: str, matching_confidence: float):
    try:
        with open('db/user_db.json', 'r') as file:
            data = json.load(file)

        data["users"].append({"user_id": user_id,
                              "user_first_name": user_first_name,
                              "user_last_name": user_last_name,
                              "last_updated": datetime.datetime.now().isoformat(),
                              "character_description": character_description,
                              "matched_archetype_index": predicted_archetype_index,
                              "matched_archetype_label": predicted_archetype_label,
                              "matching_confidence": matching_confidence})

        with open('db/user_db.json', 'w') as file:
            json.dump(data, file, indent=1)

        print("Success: This user's archetype prediction has been saved to the user database.")

        return True

    except:
        print("Error: Something went wrong in saving the user archetype prediction to the user database.")
        return False


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


