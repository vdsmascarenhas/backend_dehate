from typing import List
from app.services.platform.platform_factory import PlatformFactory
from app.interfaces.platform_interface import PlatformInterface
from app.domain.models.media import Media
from app.domain.models.comment import Comment


class PlatformService(PlatformInterface):
    def __init__(self, platform: str):
        # Inicializa a plataforma (ex: YouTube) via factory
        self.platform: PlatformInterface = PlatformFactory().get_platform(platform)
        
    # Busca todas as mídias da plataforma conectada
    async def fetch_medias(self) -> List[Media]:
        return await self.platform.fetch_medias()

    # Retorna os comentários de uma mídia específica
    async def fetch_comments(self, media_id: str) -> List[Comment]:
        return await self.platform.fetch_comments(media_id)

    # "Deleta" (ou moderar) os comentários com base nos IDs fornecidos
    async def delete_comments(self, comment_ids: List[str]) -> bool:
        return await self.platform.delete_comments(comment_ids)
