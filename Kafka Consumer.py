#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from kafka import KafkaConsumer
from time import sleep
from json import dumps, loads
import json
from s3fs import S3FileSystem

# Create a Kafka consumer
consumer = KafkaConsumer(
    'demo_test',
    bootstrap_servers=['your_kafka_ip:9092'],  # Replace 'your_kafka_ip' with the actual IP address of Kafka server
    value_deserializer=lambda x: loads(x.decode('utf-8'))
)

s3 = S3FileSystem()

# Iterate over messages received from Kafka topic 'demo_test'
for count, i in enumerate(consumer):
    # Open a file on S3 and dump the received message value as JSON
    with s3.open("s3://kafka-stock-market/stock_market_{}.json".format(count), 'w') as file:
        json.dump(i.value, file)

