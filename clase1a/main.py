from fastapi import FastAPI
import uvicorn

app=FastAPI()

@app.get("/")
def prueba():
    return{"Hola":"ITSA"}
