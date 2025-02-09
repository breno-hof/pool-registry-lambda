import uuid
from models.domains.pool_model import PoolModel
from models.requests.pool_create_request import PoolCreateRequest

def convert_request_to_domain(request: PoolCreateRequest) -> PoolModel:
		return PoolModel.model_validate({
			**request.model_dump(),         # Copia os dados do objeto original
			"pool_id": str(uuid.uuid4()),   # Gera um UUID único
			"notes": []
		})
	