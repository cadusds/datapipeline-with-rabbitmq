import os
import logging
from connection import Conn

class CreateData(Conn):
    
    DB_HOST = 'db'

    def __init__(self) -> None:
        super().__init__()
    
    def create_a_user(self):
        return self.execute('''
            insert into test (username,email) values('cadu','cadu@gmail.com'); 
        ''')

    def create_users(self,n_users):
        count = 1
        while count <= n_users:
            self.create_a_user()
            logging.warning(f'{count} - users insert')
            count += 1


CreateData().create_users(1000)