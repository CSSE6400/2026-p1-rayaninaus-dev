from flask import Blueprint, jsonify

api = Blueprint("api", __name__, url_prefix="/api/v1")

@api.route("/health")
def health():
    return jsonify({"status": "ok"})

@api.route("/todos", methods=["GET"])
def get_todos():
    return jsonify([])

@api.route("/todos/<int:id>", methods=["GET"])
def get_todo(id):
    return jsonify({"id": id})

@api.route("/todos", methods=["POST"])
def create_todo():
    return jsonify({"id": 1}), 201

@api.route("/todos/<int:id>", methods=["PUT"])
def update_todo(id):
    return jsonify({"id": id})

@api.route("/todos/<int:id>", methods=["DELETE"])
def delete_todo(id):
    return jsonify({"id": id})