from kafka import KafkaConsumer
import json

# Initialize consumer variable and set property for JSON decode
consumer = KafkaConsumer ('twitter',bootstrap_servers = ['kafka1:9092','kafka2:9093','kafka3:9094'],
value_deserializer=lambda m: json.loads(m.decode('utf-8')))

# Read data from kafka
for message in consumer:
    print(message.value)
