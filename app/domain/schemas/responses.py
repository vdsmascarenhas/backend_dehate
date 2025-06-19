from pydantic import BaseModel
from typing import Any, Dict, Generic, List, Optional, TypeVar

# Tipo genérico para dados dinâmicos em respostas
T = TypeVar('T')

# Estrutura básica para qualquer resposta
class ResponseBase(BaseModel):
    success: bool
    message: str

    class Config:
        arbitrary_types_allowed = True

# Estrutura para resposta com dado genérico
class DataResponse(ResponseBase, Generic[T]):
    data: T

# Estrutura de resposta em caso de erro com detalhes
class ErrorResponse(ResponseBase):
    errors: Optional[List[Dict[str, Any]]] = None

# Estrutura genérica para resposta paginada
class PaginatedResponse(DataResponse, Generic[T]):
    total: int
    page: int
    page_size: int
