from databases.fake_db import FakeDataBase
from databases.database_manager import DataBaseManagerProtocol

class DeletePoolUseCase:
    def __init__(self, database: DataBaseManagerProtocol):
        self.__database = database

    def delete_pool_by_id(self, pool_id: str):
        self.__database.delete_by_id(pool_id)
        
        return { }, 204
