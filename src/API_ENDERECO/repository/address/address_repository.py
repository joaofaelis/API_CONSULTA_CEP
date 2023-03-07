from src.API_ENDERECO.domain.models.address_model import AddressModel
from typing import NoReturn
from decouple import config
from src.API_ENDERECO.infrastructure.mongo.mongo_infrastructure import (
    MongoInfrastructure,
)


class AddressRepository:

    __collection_name = config("ADDRESS_COLLECTION")

    @classmethod
    async def insert_address_info(cls, address_model: AddressModel) -> NoReturn:
        conection = MongoInfrastructure.get_collection(cls.__collection_name)
        conection.insert_one(address_model)
        return

    # @classmethod
    # def insert_db(cls, collection, insert):
    #     database = cls.get_collection(collection)
    #     insertion = database.insert_one(insert)
    #     return insertion
