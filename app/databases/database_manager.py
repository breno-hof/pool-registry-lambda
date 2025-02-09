from typing import Protocol

class DataBaseManagerProtocol(Protocol):
    
    def delete_by_id(self, pool_id: str) -> None:
        ...

    def get_by_id(self, pool_id: str) -> dict:
        ...

    def save(self, entity: dict) -> dict:
        ...
