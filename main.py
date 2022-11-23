import os
import dotenv

from uuid import UUID
from controller import app

from db import connect, connection


dotenv.load_dotenv()


def uuid4():
    """Generate a random UUID."""
    return UUID(bytes=os.urandom(16), version=4)


def get_token():
    connection.cursor("SELECT * FROM TABLE users")


if __name__ == "__main__":
    connect(
        os.getenv("host"),
        os.getenv("database"),
        os.getenv("user"),
        os.getenv("password"),
    )
    token = get_token()
    app.run()
