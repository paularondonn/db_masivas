from models.user import Response


def userEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "lastname": item["lastname"],
        "email": item["email"]
    }


def usersEntity(item) -> list:
    return [userEntity(i) for i in item]


def responseEntity(response: Response) -> dict:
    return {
        "data": response.data,
        "flag": response.flag,
        "message": response.message
    }
