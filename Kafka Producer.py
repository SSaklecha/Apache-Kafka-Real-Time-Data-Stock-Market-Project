#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from kafka import KafkaProducer
from time import sleep
from json import dumps
import json

# Create a Kafka producer
producer = KafkaProducer(
    bootstrap_servers=['your_kafka_ip:9092'],  # Replace 'your_kafka_ip' with the actual IP address of Kafka server
    value_serializer=lambda x: dumps(x).encode('utf-8')
)

# Send a test message to Kafka topic 'producer_kafka'
producer.send('producer_kafka', value={'surname': 'parasdasdmar'})

# Read data from a CSV file into a pandas DataFrame
df = pd.read_csv("data/indexProcessed.csv")

# Display the first few rows of the DataFrame
df.head()

# Continuously send randomly sampled records from the DataFrame to Kafka topic 'producer_kafka'
while True:
    dict_stock = df.sample(1).to_dict(orient="records")[0]
    producer.send('producer_kafka', value=dict_stock)
    sleep(1)

# Flush any pending messages in the producer buffer to the Kafka server
producer.flush()  # Clear data from Kafka server

