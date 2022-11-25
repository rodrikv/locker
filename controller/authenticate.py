from db import get_user_by_token, connect, disconnect


def authenticated(token):
    con = connect()
    user = get_user_by_token(con, token)
    disconnect(con)
    return user