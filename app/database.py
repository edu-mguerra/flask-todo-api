from flask_pymongo import PyMongo

mongo = PyMongo()


def connect_db(app):
    app.config["MONGO_URI"] = (
        "mongodb+srv://eduguerra0202:Oe1qsdRWZ5FEYnox@cluster0.hfnd5v8.mongodb.net/todo_db?retryWrites=true&w=majority&appName=Cluster0"
    )

    mongo.init_app(app)


# poderia ter colocado a url em um arquivo .env, mas resolvi deixar assim

# aqui eu fiz a conexão com o banco de dados, por meio do mongo antlas
