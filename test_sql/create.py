from getpass import getpass
from mysql.connector import connect, Error


def create_db():  # database creation
    try:
        with connect(
                host="localhost",
                user="root",
                password="1@Qwerty"
        ) as connection:
            create_db_query = "CREATE DATABASE IF NOT EXISTS Task"
            with connection.cursor() as cursor:
                cursor.execute(create_db_query)
    except Error as e:
        print(e)


def create_tables():  # table creation
    try:
        with connect(
                host="localhost",
                user="root",
                password="1@Qwerty",
                database="Task"
        ) as connection:
            event_entity_table = """
                    CREATE TABLE IF NOT EXISTS event_entity(
                        play_id int(11) NOT NULL,
                        sport_name enum('tennis','football','hockey') CHARACTER SET latin1 DEFAULT NULL,
                        home_team varchar(140) CHARACTER SET latin1 DEFAULT NULL,
                        away_team varchar(140) CHARACTER SET latin1 DEFAULT NULL,
                        PRIMARY KEY (`play_id`)
                        )
                    """
            create_value_table = """
                    CREATE TABLE IF NOT EXISTS event_value(
                        play_id int(11) DEFAULT NULL,
                        value float(12,2) DEFAULT NULL,
                        attribute enum('P1','N','P2') DEFAULT NULL,
                        outcome enum('win','lose') DEFAULT NULL,
                        KEY `play_id` (`play_id`),
                        CONSTRAINT `event_value_ibfk_1` FOREIGN KEY (`play_id`) REFERENCES `event_entity` (`play_id`)
                    )
            """
            bid_table = """
                    CREATE TABLE IF NOT EXISTS bid(
                        b_id INT(11) NOT NULL,
                        client_number INT(11) DEFAULT NULL,
                        play_id INT(11) DEFAULT NULL,
                        amount FLOAT(12,2) DEFAULT NULL,
                        coefficient FLOAT(5,2) DEFAULT NULL,
                        PRIMARY KEY (`b_id`),
                        KEY `play_id` (`play_id`),
                        CONSTRAINT `bid_ibfk_1` FOREIGN KEY (`play_id`) REFERENCES `event_entity` (`play_id`)
                    )
            """
            with connection.cursor() as cursor:
                cursor.execute(event_entity_table)
                cursor.execute(create_value_table)
                cursor.execute(bid_table)
                connection.commit()
    except Error as e:
        print(e)
