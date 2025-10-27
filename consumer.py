import pika
import os
import json

RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "localhost")
RABBITMQ_QUEUE = os.getenv("RABBITMQ_QUEUE", "mensagens")

def callback(ch, method, properties, body):
    mensagem = json.loads(body)
    print(f"📩 Mensagem recebida: {mensagem}")

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_HOST))
    channel = connection.channel()
    channel.queue_declare(queue=RABBITMQ_QUEUE)
    channel.basic_consume(queue=RABBITMQ_QUEUE, on_message_callback=callback, auto_ack=True)
    print("👂 Aguardando mensagens. Pressione CTRL+C para sair.")
    channel.start_consuming()

if __name__ == "__main__":
    main()
