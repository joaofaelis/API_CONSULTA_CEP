from src.API_ENDERECO.repository.repository import Repository
from datetime import datetime
import requests

class Service:

    @classmethod
    def get_and_logs (cls, input):
        cep = f'https://cdn.apicep.com/file/apicep/{input}.json'
        list = requests.get(cep)
        convert = list.json()
        print(convert)
        dict_append = {
            'code': convert['code'],
            'state': convert['state'],
            'city': convert['city'],
            'district': convert['district'],
            'address': convert['address'],
            'consultation_date': datetime.now()
        }
        Repository.insert_db('Logs', dict_append)
        return convert


