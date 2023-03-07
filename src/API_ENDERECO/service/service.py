from src.API_ENDERECO.repository.address.address_repository import AddressRepository
from src.API_ENDERECO.domain.models.address_model import AddressModel
from datetime import datetime
import requests


class Address_Service:
    @classmethod
    def get_and_logs(cls, input):
        cep = f"https://viacep.com.br/ws/{input}/json/"
        list = requests.get(cep)
        convert = list.json()
        typedict: AddressModel = {
            "code": convert["cep"],
            "state": convert["uf"],
            "city": convert["localidade"],
            "district": convert["bairro"],
            "address": convert["logradouro"],
            "consultation_date": datetime.now().timestamp(),
        }
        AddressRepository.insert_address_info(typedict)
        return typedict
