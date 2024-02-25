import pika
import time
import random

conn_par = pika.ConnectionParameters('localhost')
conn = pika.BlockingConnection(conn_par)

channel = conn.channel()

channel.queue_declare(queue = 'box')
messageID = 1

while(True):
    message = f"Sending Message: {messageID}" 
    channel.basic_publish(exchange='', routing_key='box', body = message)
    print(f"sent message: {message}")
    time.sleep(random.randint(1,4))
    #conn.close()

    messageID+=1
