import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import auth as auth_router
from app.api.routes import media as media_router

# Instancia o aplicativo FastAPI
app = FastAPI(
    title=".DeHate API",
    version="1.0.0",
    description="API do .DeHate, seu app de limpeza de redes sociais."
)

# Adiciona o middleware de CORS, permitindo que
# aplicações front-end acessem essa API de outros domínios
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registra as rotas de autenticação e mídia
app.include_router(auth_router.router)
app.include_router(media_router.router)

# Ponto de entrada do servidor
if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
