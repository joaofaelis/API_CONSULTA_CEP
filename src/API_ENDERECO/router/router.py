from fastapi import APIRouter
from src.API_ENDERECO.service.service import Service

API = APIRouter()

@API.get('/')
async def insertion_cep(cep):
    find = Service.get_and_logs(cep)
    return find

