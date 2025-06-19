from pydantic import BaseModel

# Representa um comentário relacionado a uma mídia específica
class Comment(BaseModel):
    id: str
    media_id: str
    text: str

    class Config:
        orm_mode = True
