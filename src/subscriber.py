from connection import Conn
import logging
import select as sl
import pika

class Subscriber(Conn):

    channel = 'changes'

    def __init__(self) -> None:
        super().__init__()
        self.execute(f' LISTEN {self.channel}')
    
    

    def send(self,payload):
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='rabbitmq')
        )
        channel = connection.channel()

        channel.queue_declare(queue='hello')

        channel.basic_publish(
            exchange='',
            routing_key='hello',
            body=payload
        )
        connection.close()

    def db_listen(self):
        while True:
            sl.select([self.conn],[],[])   #sleep until there is some data
            self.conn.poll()                   #get the message
            while self.conn.notifies:
                notification =  self.conn.notifies.pop()  #pop notification from list
                #now do anything needed! 
                logging.warning(f"channel: {notification.channel }")
                logging.warning(f"message: {notification.payload}")
                self.send(notification.payload)

Subscriber().db_listen()