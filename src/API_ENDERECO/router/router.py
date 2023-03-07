from fastapi import APIRouter, HTTPException, status
from src.API_ENDERECO.service.service import Address_Service

API = APIRouter()


@API.get(
    "/_Consulta",
    description="Retorna a localização do CEP informado e armazena a pesquisa no banco de dados.",
)
async def insertion_cep(cep):
    try:
        find = Address_Service.get_and_logs(cep)
        return find
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Verifique novamente o CEP informado. (Apenas são aceitos CEP brasileiros).",
        )
