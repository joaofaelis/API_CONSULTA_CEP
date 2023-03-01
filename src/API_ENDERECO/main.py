from fastapi import FastAPI
from src.API_ENDERECO.router.router import API

app = FastAPI(title="API_BUSCA_ENDEREÇO",
              description='API feita para pesquisas de CEP',
              version='0.0.1')


app.include_router(API, tags=['GET_CEP'])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)