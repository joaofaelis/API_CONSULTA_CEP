from pymongo import MongoClient

class Infrastructure:

    DB = MongoClient('mongodb://localhost:27017')
    CONECTION = DB.get_database('API_ENDERECO')

    print(CONECTION)


