from typing import List
from databases.database_manager import DataBaseManagerProtocol

class FakeDataBase(DataBaseManagerProtocol):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(FakeDataBase, cls).__new__(cls)
            cls._instance.database = {
                "b7d61a1a-df64-4ed0-872c-33c57e1a14df": {
                    "pool_id": "b7d61a1a-df64-4ed0-872c-33c57e1a14df",
                    "name": "Luxury Pool",
                    "location": "Backyard",
                    "volume": 5000.0,
                    "material": "tile",
                    "heating_type": "gas",
                    "maintenance_frequency": "weekly",
                    "notes": []
                }
            }
            
        return cls._instance

    def delete_by_id(self, pool_id: str) -> None:
        self.database.pop(pool_id, None) 
        return None

    def get_by_id(self, pool_id: str) -> dict:
        return self.database.get(pool_id, None)

    def save(self, entity: dict) -> dict:
        self.database[entity["pool_id"]] = entity
        return entity