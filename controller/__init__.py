from fastapi import FastAPI, status
from controller.authenticate import authenticated
from controller.response import response_data
from commands.suspend import suspend
from db import connect, get_user_by_token

app = FastAPI()


@app.get("/ping")
def ping():
    return response_data("pong", "pong pong n**ga", status.HTTP_200_OK)


@app.post("/{token}/suspend/")
def suspend_(token: str):
    if not authenticated(token):
        code = status.HTTP_404_NOT_FOUND
        return response_data(data="not found", msg="user not found", code=code), code

    try:
        suspend()
        code = status.HTTP_200_OK
        return response_data(data="ok", msg="ok", code=code), code
    except:
        code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response_data(data="", msg="something went wrong", code=code), code
