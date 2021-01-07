import sys, pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='direct_logs', exchange_type='direct')
severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'
if severity == "Danger":
    channel.basic_publish(exchange='direct_logs', routing_key='Danger', body=message)
else:
    channel.basic_publish(exchange='direct_logs', routing_key='Simple', body=message)
print('Sent message', message, severity)
connection.close()