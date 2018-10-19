import pika, sys

credentials = pika.PlainCredentials("guest", "guest")
conn_params = pika.ConnectionParameters("localhost", credentials = credentials)
conn_broker = pika.BlockingConnection(conn_params)

channel = conn_broker.channel()
channel.exchange_declare(exchange="hello-exchange", exchange_type="direct", passive=False, durable=True, auto_delete=False)

msg = sys.argv[1]
msg_props = pika.BasicProperties()
msg_props.content_type = "text/plain"

channel.basic_publish(exchange="hello-exchange", routing_key="hola", body=msg, properties=msg_props)