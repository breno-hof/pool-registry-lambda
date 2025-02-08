from databases.fake_db import FakeDataBase

class DeletePoolUseCase:
    
    @staticmethod
    def delete_pool_by_id(pool_id: str):
        database = FakeDataBase()
        database.delete_by_id(pool_id)
        
        return { }, 204  # Retorna JSON válido
