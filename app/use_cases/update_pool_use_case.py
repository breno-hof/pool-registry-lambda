import json
from aws_lambda_powertools import Logger
from models.requests.pool_update_request import PoolUpdateRequest
from models.domains.pool_model import PoolModel
from mappers.domain_to_response import convert_domain_to_response
from databases.database_manager import DataBaseManagerProtocol

class UpdatePoolUseCase:
    logger = Logger()
    
    def __init__(self, database: DataBaseManagerProtocol):
        self.__database = database

    def update_pool_by_id(self, pool_id: str, request: PoolUpdateRequest):
        entity = self.__database.get_by_id(pool_id)
        if entity == None:
            return {"error": "Pool not found"}, 404
        
        updated_notes = entity["notes"] + request.notes
        if len(updated_notes) > 10:
            updated_notes = request.notes

        filtered_entity = { key: value for key, value in request.model_dump().items() if value is not None }
        updated_entity = entity | { **filtered_entity, "notes": updated_notes }

        domain = PoolModel(**updated_entity)
        self.__database.save(domain.model_dump())
        
        response = convert_domain_to_response(domain)

        return { "data": response.model_dump() }, 200  
