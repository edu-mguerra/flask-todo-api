from flask_pymongo import PyMongo

mongo = PyMongo()


def connect_db(app):
    app.config["MONGO_URI"] = (
        "mongodb+srv://eduguerra0202:Oe1qsdRWZ5FEYnox@cluster0.hfnd5v8.mongodb.net/todo_db?retryWrites=true&w=majority&appName=Cluster0"
    )

    mongo.init_app(app)
