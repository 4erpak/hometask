from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['kafka1:9092','kafka2:9093','kafka3:9094'])

for _ in range(100):
    producer.send('new-cool-topic', b'cool-message')
producer.flush()
