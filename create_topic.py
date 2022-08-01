from kafka.admin import KafkaAdminClient, NewTopic

admin_client = KafkaAdminClient(
        bootstrap_servers=['kafka1:9092','kafka2:9093','kafka3:9094']
)
topic_list = [NewTopic(name="new-cool-topic", num_partitions=1, replication_factor=3)]
admin_client.create_topics(new_topics=topic_list, validate_only=False)
