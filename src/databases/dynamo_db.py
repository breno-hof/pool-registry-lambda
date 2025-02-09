from aws_lambda_powertools import Logger
from databases.database_manager import DataBaseManagerProtocol
import boto3

class DynamoDB(DataBaseManagerProtocol):
	_instance = None
	logger = Logger()
			
	def __new__(cls, tableName):
		if cls._instance is None:
			cls._instance = super().__new__(cls)
			cls.__dynamodb = boto3.resource("dynamodb")

		cls.__table = cls.__dynamodb.Table(tableName)

		return cls._instance

	def delete_by_id(self, pool_id: str) -> None:
		self.__table.delete_item(Key={"pool_id": pool_id})
		self.logger.info("item deleted from table", pool_id)
		return None

	def get_by_id(self, pool_id: str) -> dict:
		response = self.__table.get_item(Key={"pool_id": pool_id}).get("Item")
		self.logger.info("item get from table", response)
		return response

	def save(self, entity: dict) -> dict:
		self.__table.put_item(Item=entity)
		self.logger.info("item created", entity)
		return entity