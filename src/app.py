from aws_lambda_powertools.event_handler import APIGatewayHttpResolver
from pydantic import ValidationError
from use_cases.create_pool_use_case import CreatePoolUseCase
from use_cases.update_pool_use_case import UpdatePoolUseCase
from use_cases.delete_pool_use_case import DeletePoolUseCase
from models.requests.pool_create_request import PoolCreateRequest
from models.requests.pool_update_request import PoolUpdateRequest

app = APIGatewayHttpResolver()

@app.put("/pools/<pool_id>")
def update_pool_by_id(pool_id: str):
    try:
        request = PoolUpdateRequest(**app.current_event.json_body)
        return UpdatePoolUseCase.update_pool_by_id(pool_id, request)
    
    except (ValidationError, TypeError) as e:
        return { "error": str(e) }, 400
    
    except Exception as e:
        return { "error": str(e) }, 500

@app.delete("/pools/<pool_id>")
def delete_pool_by_id(pool_id: str):
    try:
        return DeletePoolUseCase.delete_pool_by_id(pool_id)
    
    except (ValidationError, TypeError) as e:
        return { "error": str(e) }, 400
    
    except Exception as e:
        return { "error": str(e) }, 500

@app.post("/pools")
def create_pool():
    try:
        request = PoolCreateRequest(**app.current_event.json_body)
        return CreatePoolUseCase.create_pool(request)
    
    except (ValidationError, TypeError) as e:
        return { "error": str(e) }, 400
    
    except Exception as e:
        return { "error": str(e) }, 500
    

def lambda_handler(event, context):
    try:
        return app.resolve(event, context)

    except Exception as e:
        return { "error": str(e) }, 500
    
    
    
   