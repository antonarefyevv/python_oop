from fastapi import FastAPI, HTTPException, Depends, Header
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from passlib.hash import bcrypt

app = FastAPI()

# Имитация базы данных пользователей
users = {
    "john@example.com": {
        "password": bcrypt.hash("secret123"),
        "salary": 1000,
        "next_raise_date": "2023-06-01"
    },
    "jane@example.com": {
        "password": bcrypt.hash("secret456"),
        "salary": 1500,
        "next_raise_date": "2023-09-01"
    },
}

security = HTTPBasic()


@app.post("/token")
async def get_token(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username not in users:
        raise HTTPException(status_code=401, detail="Неверный логин")

    if not bcrypt.verify(credentials.password, users[credentials.username]["password"]):
        raise HTTPException(status_code=401, detail="Неверный пароль")

    return {"token": "секретный_токен"}


@app.get("/salary", dependencies=[Depends(security)])
async def get_salary(token: str = Depends(Header(...))):
    if token != "секретный_токен":
        raise HTTPException(status_code=401, detail="Неверный токен")

    username = security.credentials.username
    return {"salary": users[username]["salary"]}


@app.get("/next_raise_date", dependencies=[Depends(security)])
async def get_next_raise_date(token: str = Depends(Header(...))):
    if token != "секретный_токен":
        raise HTTPException(status_code=401, detail="Неверный токен")

    username = security.credentials.username
    return {"next_raise_date": users[username]["next_raise_date"]}
