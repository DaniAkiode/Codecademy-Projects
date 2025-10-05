from flask import Blueprint, jsonify, request
from models.user_model import get_all_users, add_user, update_user, delete_user

user_bp = Blueprint("user", __name__)

@user_bp.route("/", methods=["GET"])
def get_users():
    return jsonify(get_all_users())

@user_bp.route("/", methods=["POST"])
def create_user():
    data = request.json
    new_user = add_user(data)
    return jsonify({"message": "User added", "user": new_user}), 201

@user_bp.route("/<int:user_id>", methods=["PUT"])
def modify_user(user_id):
    data = request.json
    updated_user = update_user(user_id, data)
    if updated_user:
        return jsonify({"message": "User updated", "user" : updated_user})
    return jsonify({"error": "User not found"}), 404

@user_bp.route("/<int:user_id>", methods=["DELETE"])
def remove_user(user_id):
    deleted_user = delete_user(user_id)
    if deleted_user:
        return jsonify({"message": "User deleted", "user": deleted_user})
    return jsonify({"error": "User not found"}), 404

