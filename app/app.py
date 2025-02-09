from aws_lambda_powertools import Logger
from aws_lambda_powertools.event_handler import (APIGatewayHttpResolver, Response, content_types)
from pydantic import ValidationError
from use_cases.create_pool_use_case import CreatePoolUseCase
from use_cases.update_pool_use_case import UpdatePoolUseCase
from use_cases.delete_pool_use_case import DeletePoolUseCase
from models.requests.pool_create_request import PoolCreateRequest
from models.requests.pool_update_request import PoolUpdateRequest
from databases.dynamo_db import DynamoDB

app = APIGatewayHttpResolver()
logger = Logger()

database = DynamoDB("pool_registry_table")

@app.put("/pools/<pool_id>")
def update_pool_by_id(pool_id: str):
	update_use_case = UpdatePoolUseCase(database)

	request = PoolUpdateRequest(**app.current_event.json_body)

	return update_use_case.update_pool_by_id(pool_id, request)

@app.delete("/pools/<pool_id>")
def delete_pool_by_id(pool_id: str):
	delete_use_case = DeletePoolUseCase(database)
	
	return delete_use_case.delete_pool_by_id(pool_id)

@app.post("/pools")
def create_pool():
	create_use_case = CreatePoolUseCase(database)

	request = PoolCreateRequest(**app.current_event.json_body)

	return create_use_case.create_pool(request)

@app.exception_handler(ValidationError)
def handle_validation_error(error: ValidationError):
	logger.warning(error)
	return Response(
		status_code=400,
		content_type=content_types.APPLICATION_JSON,
		body={ "errors": [{"field": err["loc"][0], "message": err["msg"]} for err in error.errors()] }
	)

@app.exception_handler(Exception)
def handle_interal_error(error: Exception):
	logger.error(error)
	return Response(
		status_code=500,
		content_type=content_types.APPLICATION_JSON,
		body={ "error": str(error) }
	)

def lambda_handler(event, context):
	return app.resolve(event, context)