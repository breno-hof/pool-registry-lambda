from models.requests.pool_update_request import PoolUpdateRequest
from databases.fake_db import FakeDataBase
from models.domains.pool_model import PoolModel
from mappers.domain_to_response import convert_domain_to_response

class UpdatePoolUseCase:
    
    @staticmethod
    def update_pool_by_id(pool_id: str, request: PoolUpdateRequest):
        database = FakeDataBase()
        entity = database.get_by_id(pool_id)
        
        if entity == None:
             return {"error": "Pool not found"}, 404
        
        updated_entity = entity | request.model_dump()

        domain = PoolModel(**updated_entity)
        database.save(domain.model_dump())
        
        response = convert_domain_to_response(domain)

        return { "data": response.model_dump() }, 200  
