from kafka import KafkaConsumer

consumer = KafkaConsumer('new-cool-topic',bootstrap_servers=['kafka1:9092','kafka2:9093','kafka3:9094'])
for message in consumer:
    print (message.value)
