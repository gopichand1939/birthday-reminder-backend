from flask import Blueprint, request, jsonify
from models.db import collection
from bson import ObjectId
from datetime import datetime

birthday_bp = Blueprint("birthday_bp", __name__)

# Add new birthday entry
@birthday_bp.route("/birthday", methods=["POST"])
def add_birthday():
    data = request.json
    name = data.get("name")
    email = data.get("email")
    dob = data.get("dob")  # YYYY-MM-DD
    send_at = data.get("sendAt")  # Format: 2025-05-17T12:08

    if not name or not email or not dob or not send_at:
        return jsonify({"error": "All fields are required"}), 400

    birthday = {
        "name": name,
        "email": email,
        "dob": dob,
        "sendAt": send_at,  # New: exact timestamp for sending
        "emailSent": False,
        "created_at": datetime.utcnow()
    }

    collection.insert_one(birthday)
    return jsonify({"message": "Birthday added successfully"}), 201

# View all entries
@birthday_bp.route("/birthdays", methods=["GET"])
def get_birthdays():
    birthdays = list(collection.find())
    for b in birthdays:
        b["_id"] = str(b["_id"])
    return jsonify(birthdays)

# Delete an entry by ID
@birthday_bp.route("/birthday/<id>", methods=["DELETE"])
def delete_birthday(id):
    result = collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 1:
        return jsonify({"message": "Deleted successfully"})
    return jsonify({"error": "Not found"}), 404
