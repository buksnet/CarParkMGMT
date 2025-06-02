from psycopg2 import connect
from application.config import DATABASE_URL, DATABASE_PORT, DATABASE_PASSWORD, DATABASE_NAME, DATABASE_USER
from yaml import safe_load as yaml_load


# noinspection PyUnresolvedReferences
class BaseController:
    def __init__(self):
        self.connection = connect(host=DATABASE_URL, user=DATABASE_USER,
                                  password=DATABASE_PASSWORD, dbname=DATABASE_NAME, port=DATABASE_PORT)

    def submit_query(self, query: str, is_unitary: bool = True) -> tuple:
        """
        Отправляет запрос в базу данных и возвращает ответ

        :param query: запрос в формате строки
        :param is_unitary: является ли ожидаемый результат итерируемым
        :return: кортеж с результатами выполнения запроса
        """
        with self.connection.cursor() as cursor:
            cursor.execute(query)

            if is_unitary:
                result: tuple
                result = cursor.fetchone()
            else:
                result: list[tuple] = cursor.fetchall()

        return result


class Controller(BaseController):
    def __init__(self):
        super().__init__()
        self.__create_all()

    def __create_all(self):
        """
        Создаёт все необходимые для работы таблицы в базе данных при необходимости

        :return:
        """

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
                with self.connection.cursor() as cursor:
                    cursor.execute(table)
                    self.connection.commit()

            except Exception as e:
                self.connection.rollback()
                print(e, table, sep='\n')
                break
