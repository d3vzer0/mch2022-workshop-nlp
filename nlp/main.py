from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from routers.v1.main import api_v1

# Initialise FastAPI + CORS 
app = FastAPI(
    title='MCH2022 NLP',
    description='Using NLP for vulnerability monitorng',
)

# Init CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['POST'],
    allow_headers=["*"],
)

# Include v1 endpoints
app.include_router(api_v1, prefix='/api/v1')