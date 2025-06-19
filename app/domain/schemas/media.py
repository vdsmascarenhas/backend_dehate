from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional, Literal
from app.domain.models.media import MediaType

# Base comum para representação de mídia (utilizada em respostas)
class MediaBase(BaseModel):
    id: str 
    format: MediaType
    image: str
    title: str
    publish_date: datetime
    view_count: int
    comment_count: int
    like_count: int

# Schema de resposta para uma mídia
class MediaResponse(MediaBase):
    pass

# Schema que representa a resposta da listagem de mídias
class MediasListResponse(BaseModel):
    videos: List[MediaResponse]
    total: int

# Parâmetros que podem ser usados para filtrar as mídias
class MediaFilterParams(BaseModel):
    format: Optional[MediaType] = None
    min_views: Optional[int] = None
    max_views: Optional[int] = None
    min_comments: Optional[int] = None
    max_comments: Optional[int] = None
    min_likes: Optional[int] = None
    max_likes: Optional[int] = None
    sort_by: Optional[Literal["date","views","comments","likes"]] = "date"
    sort_order: Optional[Literal["asc","desc"]] = "desc"
