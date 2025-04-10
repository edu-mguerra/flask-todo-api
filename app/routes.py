from flask import Blueprint, request, jsonify
from bson import ObjectId
from datetime import datetime
from .database import mongo

tasks_bp = Blueprint("tasks", __name__)


@tasks_bp.route("/tasks", methods=["POST"])  # define a rota para a função abaixo
def create_task():
    data = request.get_json()  # pega o json que enviamos no  body

    required_fields = [  # verifica se os campos estão presentes
        "title",
        "description",
        "status",
        "owner",
    ]
    if not all(field in data for field in required_fields):
        return (
            jsonify({"error": "Campos obrigatórios faltando"}),
            400,
        )  # Se algum estiver faltando, retorna um erro 400 (Bad Request)

    # Campos válidos de status
    if data["status"] not in ["done", "in_progress", "pending"]:
        return jsonify({"error": "Status inválido"}), 400

    new_task = {
        "title": data["title"],
        "description": data["description"],
        "status": data["status"],
        "owner": data["owner"],
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow(),
    }

    result = mongo.db.tasks.insert_one(new_task)  # insere a taks do banco de dados
    new_task["_id"] = str(result.inserted_id)  # recupera o id e transforma em sting

    return jsonify(new_task), 201


@tasks_bp.route("/tasks", methods=["GET"])
def get_tasks():
    status = request.args.get("status")  # pega o valor/valores da URl
    query = {}
    if status:  # cria uma query vazia e se o status foi informado, preenche com o valor
        query["status"] = status

    tasks_cursor = mongo.db.tasks.find(query).sort(
        "created_at", -1
    )  # buscas as tarefas de acordo com o mais recente
    tasks = []

    for task in tasks_cursor:
        tasks.append(
            {
                "_id": str(task["_id"]),
                "title": task["title"],
                "description": task["description"],
                "status": task["status"],
                "owner": task["owner"],
                "created_at": task["created_at"],
                "updated_at": task["updated_at"],
            }
        )

    return jsonify(tasks), 200


@tasks_bp.route(
    "/tasks/<task_id>", methods=["GET"]
)  # aqui é passado um valor dinamico para a URL
def get_task(task_id):
    try:
        task = mongo.db.tasks.find_one(
            {"_id": ObjectId(task_id)}
        )  # busca a tarefa pelo o ID

        if not task:
            return jsonify({"error": "Tarefa não encontrada"}), 404

        task["_id"] = str(task["_id"])
        return jsonify(task), 200

    except:
        return jsonify({"error": "ID inválido"}), 400


@tasks_bp.route(
    "/tasks/<task_id>", methods=["PUT"]
)  # aqui é passado um valor dinamico para a URL, o id
def update_task(task_id):
    data = request.get_json()
    try:
        update_fields = {}

        # Atualiza apenas os campos válidos
        if "title" in data:
            update_fields["title"] = data["title"]
        if "description" in data:
            update_fields["description"] = data[
                "description"
            ]  # Se o JSON contém "title" ou "description", adiciona esses campos ao update_fields.

        if "status" in data:  # apenas um formato valalido
            if data["status"] not in ["done", "in_progress", "pending"]:
                return jsonify({"error": "Status inválido"}), 400
            update_fields["status"] = data["status"]
        if update_fields == {}:
            return jsonify({"error": "Nada para atualizar"}), 400

        update_fields["updated_at"] = datetime.utcnow()

        result = mongo.db.tasks.update_one(
            {"_id": ObjectId(task_id)}, {"$set": update_fields}
        )  # Realiza a atualização no banco usando o $set

        if result.matched_count == 0:
            return jsonify({"error": "Tarefa não encontrada"}), 404

        return jsonify({"message": "Tarefa atualizada com sucesso"}), 200

    except:
        return jsonify({"error": "ID inválido"}), 400


@tasks_bp.route(
    "/tasks/<task_id>", methods=["DELETE"]
)  # busca a taks pelo o id e deleta
def delete_task(task_id):
    try:
        result = mongo.db.tasks.delete_one({"_id": ObjectId(task_id)})

        if result.deleted_count == 0:
            return jsonify({"error": "Tarefa não encontrada"}), 404

        return jsonify({"message": "Tarefa deletada com sucesso"}), 200

    except:
        return jsonify({"error": "ID inválido"}), 400
