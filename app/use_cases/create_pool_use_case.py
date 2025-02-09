from aws_lambda_powertools import Logger
from models.requests.pool_create_request import PoolCreateRequest
from mappers.domain_to_response import convert_domain_to_response
from mappers.request_to_domain import convert_request_to_domain
from databases.database_manager import DataBaseManagerProtocol

class CreatePoolUseCase:
	def __init__(self, database: DataBaseManagerProtocol):
		self.__database = database

	def create_pool(self, request: PoolCreateRequest):		
		domain = convert_request_to_domain(request)

		self.__database.save(domain.model_dump())
		
		response = convert_domain_to_response(domain)
		
		return { "data": response.model_dump() }, 201
	