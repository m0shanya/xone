from prettytable import PrettyTable

from create import create_db, create_tables
from delete import delete_db, delete_tables  # для последующего удаления таблиц и БД
from mysql.connector import connect, Error

create_db()
create_tables()
"""
Заполняю таблицы из дампа /down/Тестовое задание Python Django/sql/test_task_sql.sql
командой mysql -u username -p Task < test_task_sql.sql
"""


def task_1():
    # connecting to DB
    try:
        with connect(
                host="localhost",
                user="root",
                password="1@Qwerty",
                database="Task"
        ) as connection:
            # request generation
            task_1_query = """SELECT client_number as client,
                                SUM(outcome = 'win') as win,
                                SUM(outcome = 'lose') as lose
                        FROM bid
                        INNER JOIN event_value
                        ON bid.play_id = event_value.play_id
                        GROUP BY client_number; """

            with connection.cursor() as cursor:
                cursor.execute(task_1_query)
                result = cursor.fetchall()  # чтение результата execute

            head = ['client_number', 'Побед', 'Поражений']  # table column names
            table = PrettyTable(head)  # table generation

            for c, win, lose in result:
                table.add_row((c, win, lose))  # inserting data into table row's

            print(table)
    except Error as e:
        print(e)


def task_2():
    # connecting to DB
    try:
        with connect(
                host="localhost",
                user="root",
                password="1@Qwerty",
                database="Task"
        ) as connection:
            # request generation
            task_2_query = """SELECT least(home_team, away_team) AS A, 
                                  greatest(home_team, away_team) AS B, 
                                  COUNT(*)
                        FROM event_entity
                        GROUP BY A, B
                        ORDER BY A, B"""

            with connection.cursor() as cursor:
                cursor.execute(task_2_query)
                result = cursor.fetchall()  # чтение результата execute

            head = ['game', 'games_count']  # table column names
            table = PrettyTable(head)  # table generation

            for game1, game2, count in result:
                game = game1 + ' - ' + game2
                table.add_row((game, count))  # inserting data into table row's

            print(table)
    except Error as e:
        print(e)


while True:
    ch = int(input("Task 1 or Task 2?"))
    if (ch < 1) or (ch > 2):
        print("Input only 1 or 2!!!")
        ch = int(input("Task 1 or Task 2?"))

    if ch == 2:
        task_2()
    task_1()

    e = input("Would you like to continue?\n(type No to exit)\n")
    if e == "No":
        break
