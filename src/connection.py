import os
import logging
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

class Conn:

    DB_NAME:str = os.getenv('DB_NAME')
    DB_USER:str = os.getenv('DB_USER')
    DB_HOST:str = 'db'
    DB_PASSWORD:str = os.getenv('DB_PASSWORD')
    DB_PORT:str = 5432

    def __init__(self) -> None:
        self.conn = self._get_conn()
        self.cur = self.conn.cursor()
    
    def _get_conn(self):
        loop = True
        while loop:
            try:
                conn = psycopg2.connect(
                    dbname=self.DB_NAME,
                    user=self.DB_USER,
                    host=self.DB_HOST,
                    port=self.DB_PORT,
                    password=self.DB_PASSWORD
                )
                logging.warning('Success!!!')
                loop = False
                conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

            except psycopg2.OperationalError as e:
                logging.warning(e)

        return conn
    
    def execute(self,sql):
        self.cur.execute(sql)

