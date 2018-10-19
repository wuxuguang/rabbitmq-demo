import pika, sys
from pika import spec

credentials = pika.PlainCredentials("guest", "guest")
conn_params = pika.ConnectionParameters("localhost", credentials = credentials)
conn_broker = pika.BlockingConnection(conn_params)

channel = conn_broker.channel()
channel.exchange_declare(exchange="hello-exchange", exchange_type="direct", passive=False, durable=True, auto_delete=False)

def confirm_handler(frame):
    if type(frame.method) == spec.Confirm.SelectOk:
        print("channel in 'confirm' mode")
    elif type(frame.method == spec.Basic.Nack):
        if frame.method.deliver_tag in msg_ids:
            print("Message Lost")
    elif type(frame.method) == spec.Basic.Ack:
        print("Confirm received!")
        msg_ids.remove(frame.method.deliver_tag)

channel.confirm_delivery(confirm_handler)


msg = sys.argv[1]
msg_props = pika.BasicProperties()
msg_props.content_type = "text/plain"

msg_ids = []

channel.basic_publish(exchange="hello-exchange", routing_key="hola", body=msg, properties=msg_props)

msg_ids.append(len(msg_ids) + 1)
channel.close()