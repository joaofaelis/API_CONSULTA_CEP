from src.API_ENDERECO.infrastructure.infra import Infrastructure


DB = Infrastructure.CONECTION

class Repository:

    @classmethod
    def get_collection(cls, collection):
        conection = DB.get_collection(collection)
        return conection

    @classmethod
    def insert_db(cls, collection, insert):
        database = cls.get_collection(collection)
        insertion = database.insert_one(insert)
        return insertion


