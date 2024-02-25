import pika
import time
import random

def message_received(ch, method, properties, body):
    processing_time = random.randint(1, 6)
    print(f"message received: {body}, will take {processing_time} to process")
    time.sleep(processing_time)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print("Finished Processing")

conn_par = pika.ConnectionParameters('localhost')
conn = pika.BlockingConnection(conn_par)

channel = conn.channel()

channel.queue_declare(queue = 'box')

channel.basic_qos(prefetch_count=1)

channel.basic_consume(queue = 'box', on_message_callback=message_received)

print("Started Consuming")
channel.start_consuming()
