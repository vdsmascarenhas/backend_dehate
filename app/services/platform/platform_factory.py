from app.infrastructure.clients.youtube_client import YouTubeClient
from app.interfaces.platform_interface import PlatformInterface
from app.interfaces.auth_interface import AuthInterface


class PlatformFactory:
    @staticmethod
    def get_platform(platform: str) -> PlatformInterface | AuthInterface:
        # Cria e retorna uma instância da plataforma escolhida (ex: YouTube)
        if platform.lower() == "youtube":
            return YouTubeClient()
        else:
            raise ValueError(
                f"Plataforma '{platform}' não suportada no momento."
            )
        