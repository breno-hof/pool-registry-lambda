from models.requests.pool_create_request import PoolCreateRequest
from mappers.domain_to_response import convert_domain_to_response
from mappers.request_to_domain import convert_request_to_domain
from databases.fake_db import FakeDataBase
import json

class CreatePoolUseCase:

	@staticmethod
	def create_pool(request: PoolCreateRequest):
		domain = convert_request_to_domain(request)

		database = FakeDataBase()
		database.save(domain.model_dump())
		
		response = convert_domain_to_response(domain)
		
		return { "data": response.model_dump() }, 201
	