import pika, json

params = pika.URLParameters('amqps://jfrectld:d3Ok2Y_HCqGn9YqQ20KuBrAaSLPQOca8@fish.rmq.cloudamqp.com/jfrectld')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)