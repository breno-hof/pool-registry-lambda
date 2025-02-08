from models.domains.pool_model import PoolModel
from models.responses.pool_response import PoolResponse

def convert_domain_to_response(domain: PoolModel) -> PoolResponse:
    return PoolResponse.model_validate(domain.model_dump())