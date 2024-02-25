import pika
from pika.exchange_type import ExchangeType

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange='routing', exchange_type=ExchangeType.direct)

message = "It needs to be routed"

channel.basic_publish(exchange='routing', routing_key='analyticsonly', body=message)

print(f"Sent Message: {message}")
connection.close()
