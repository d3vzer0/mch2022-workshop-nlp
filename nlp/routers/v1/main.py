from fastapi import APIRouter, Depends, Security
from .predict import main as Predict

api_v1 = APIRouter()

api_v1.include_router(Predict.router,
    tags=['predict']
)