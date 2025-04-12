from pymongo import MongoClient

class MongoConnection:
    def __init__(self, db_name: str):
        self.uri = "mongodb+srv://hardikkumarsinha:ajd6nUABlRjA7cTK@cluster0.12mot7c.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        self.client = MongoClient(self.uri)
        self.db = self.client[db_name]
        print(f"[MongoDB] Connected to '{db_name}'")

    def get_collection(self, collection_name: str):
        return self.db[collection_name]

    def close(self):
        self.client.close()
        print("[MongoDB] Connection closed")
