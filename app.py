from fastapi import FastAPI, Form
import beyonic  

app = FastAPI()

beyonic.api_key = '674c837dcf2c02d4ff530c1fb1f24676df69cd2d'

@app.post("/login/")
async def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username}


@app.get("/currencies")
def currencies():
    currencies = beyonic.Currency.list()
    return currencies
