from psycopg2 import connect
from application.config import DATABASE_URL, DATABASE_PORT, DATABASE_PASSWORD, DATABASE_NAME, DATABASE_USER
from yaml import safe_load as yaml_load


# noinspection PyUnresolvedReferences
class Controller:
    def __init__(self):
        self.connection = connect(host=DATABASE_URL, user=DATABASE_USER,
                                  password=DATABASE_PASSWORD, dbname=DATABASE_NAME, port=DATABASE_PORT)

        self.cursor = self.connection.cursor()

    def submit_query(self, query: str, is_unitary: bool = True, do_commit: bool = True) -> tuple:
        """
        Отправляет запрос в базу данных и возвращает ответ

        :param query: запрос в формате строки
        :param is_unitary: является ли ожидаемый результат единичным
        :return: кортеж с результатами выполнения запроса
        """

        self.cursor.execute(query)

        if is_unitary:
            result: tuple
            result = self.cursor.fetchone()
        else:
            result: list[tuple] = self.cursor.fetchall()
        return result

    def create_all(self):
        with open('application/models/queries/tables.yaml') as tables:
            database_tables = yaml_load(tables)['sql']
        commits_ordered = [
            database_tables['teams'],
            database_tables['employees'],
            database_tables['team_repair_assignments'],
            database_tables['part_sets'],
            database_tables['parts'],
            database_tables['add_supervisor_fk'],
            database_tables['routes'],
            database_tables['vehicle_categories'],
            database_tables['garages'],
            database_tables['vehicles'],
            database_tables['repairs'],
            database_tables['route_assignments'],
            database_tables['drivers'],
            database_tables['driver_assignments'],
            database_tables['mileage_log'],
            database_tables['add_mileage_fk']
        ]

        for table in commits_ordered:
            try:
                self.cursor.execute(table)
                self.connection.commit()

            except Exception as e:
                self.connection.rollback()
                print(e, table, sep='\n')
                break
