import psycopg2

def connect(host, database, user, password):
    if not connection:
        connection = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password,
        )
    return connection
