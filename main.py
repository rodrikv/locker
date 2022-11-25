import os
import dotenv
import uvicorn
import logging

from uuid import UUID

from db import create_user, connect, get_user, disconnect, migrate


logger = logging.getLogger()


dotenv.load_dotenv()


def uuid4():
    """Generate a random UUID."""
    return UUID(bytes=os.urandom(16), version=4).hex


if __name__ == "__main__":
    migrate()

    con = connect()
    if not get_user(con):
        create_user(con, os.getenv("name", "default"), uuid4())
    user = get_user(con)
    disconnect(con)

    print(f"Name: {user.name} >> TOKEN: {user.token}")

    uvicorn.run(
        "controller:app",
        port=8585,
        host="0.0.0.0",
    )
