import pika
from pika.exchange_type import ExchangeType

connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)

channel= connection.channel()
#channel.queue_declare(queue='letterbox')
channel.exchange_declare(exchange='pubsub', exchange_type=ExchangeType.fanout)
message = "Hello: Message Broadcast"

channel.basic_publish(exchange='pubsub', routing_key='', body=message)
print(f"sent message: {message}")

connection.close()