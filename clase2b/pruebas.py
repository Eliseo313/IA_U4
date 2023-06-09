import requests

BASE_URL = "http://127.0.0.1:8000"

def peticion_1():
    #respuesta = requests.get(BASE_URL + "/peticion-1?edad=2")
    respuesta = requests.get(BASE_URL + "/peticion-1",params={
        "edad":22,
        "estado": "michoacan",
        "estudiante": False
    })
    print(respuesta.json())


def peticion_2():
    #respuesta = requests.get(BASE_URL + "/peticion-1?edad=2")
    respuesta = requests.get(BASE_URL + "/peticion-2",params={
        "edad":44,
        "estado": "michoacán"
        #"estudiante": False
    })
    print(respuesta.json())

def body_1():
    respuesta = requests.post(BASE_URL + "/body-1",json={
        "edad" : 1,
        "nombre" : "Eliseo"
    })
    print(respuesta.json())

#peticion_1()
#peticion_2()
body_1()