from typing import List, Protocol, Set

class DataBaseManagerProtocol(Protocol):
    
    def get_filter(self, filter: Set[str]) -> List[dict]:
        ...
    
    def delete_by_id(self, pool_id: str) -> None:
        ...

    def get_by_id(self, pool_id: str) -> dict:
        ...

    def save(self, entity: dict) -> dict:
        ...
