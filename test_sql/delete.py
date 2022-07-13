from getpass import getpass
from mysql.connector import connect, Error


def delete_db():
    try:
        with connect(
                host="localhost",
                user=input("Input username: "),
                password=getpass("Input password: ")
        ) as connection:
            drop_db_query = "DROP DATABASE IF EXISTS Task"
            with connection.cursor() as cursor:
                cursor.execute(drop_db_query)
    except Error as e:
        print(e)


def delete_tables():
    try:
        with connect(
                host="localhost",
                user=input("Input username: "),
                password=getpass("Input password: "),
                database="Task"
        ) as connection:
            tables_query = """
                    DROP TABLE IF EXISTS event_entity, event_value, bid
                    """
            with connection.cursor() as cursor:
                cursor.execute(tables_query)
                connection.commit()
    except Error as e:
        print(e)
