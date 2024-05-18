from fastapi import APIRouter
from config.db import collection_user
from schemas.user import userEntity, usersEntity, responseEntity
from models.user import CreateUser, Response
from bson import ObjectId

user = APIRouter()


@user.get('/users', response_model=Response, tags=["users"])
def find_all_user():
    data = usersEntity(collection_user.find())
    flag = data is not None
    message = "Listado consultado con éxito" if flag else "No se encontró información"
    response = Response(data=data, flag=flag, message=message)

    return responseEntity(response)


@user.post('/users/create', response_model=Response, tags=["users"])
def create_user(user: CreateUser):
    new_user = dict(user)
    id = collection_user.insert_one(new_user).inserted_id

    data = userEntity(collection_user.find_one({"_id": id}))
    flag = data is not None
    message = "Listado consultado con éxito" if flag else "No se encontró información"

    response = Response(data=data, flag=flag, message=message)

    return responseEntity(response)


@user.get('/users/find/{id}', response_model=Response, tags=["users"])
def find_user(id: str):
    detail = collection_user.find_one({"_id": ObjectId(id)})

    data = userEntity(detail)
    flag = data is not None
    message = "Detalle de usuario consultado con exito" if flag else "No se encontró información"

    response = Response(data=data, flag=flag, message=message)

    return responseEntity(response)


@user.put('/users/update/{id}', response_model=Response, tags=["users"])
def update_user(id: str, user: CreateUser):
    collection_user.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(user)})

    detail = collection_user.find_one({"_id": ObjectId(id)})

    data = userEntity(detail)
    flag = data is not None
    message = "Actualización de usuario exitosa" if flag else "Ocurrio un error, no se pudo actualizar usuario"

    response = Response(data=data, flag=flag, message=message)

    return responseEntity(response)


@user.delete('/users/delete/{id}', response_model=Response, tags=["users"])
def delete_user(id: str):
    collection_user.find_one_and_delete({"_id": ObjectId(id)})

    detail = collection_user.find_one({"_id": ObjectId(id)})

    data = None
    flag = detail is None
    message = "Eliminación de usuario realizada con exito" if flag else "Ocurrio un error, no se pudo eliminar usuario"

    response = Response(data=data, flag=flag, message=message)

    return responseEntity(response)
