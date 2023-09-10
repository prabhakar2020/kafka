"""
@Author: Prabhakar
@Date: Sept 10, 2023
Description: File to add messages to given topic in Kafka
""" 

from time import sleep  
from json import dumps  
from kafka import KafkaProducer  

my_producer = KafkaProducer(  
    bootstrap_servers = ['localhost:9092'],  
    value_serializer = lambda x:dumps(x).encode('utf-8') ,
    retries=2
     
    )  

for n in range(int(input("Start Number: ")), int(input("End Number: "))+1):  
    my_data = {'num' : n}  
    print (my_data)
    my_producer.send('my_group', value = my_data, timestamp_ms=123)  
    # Sleep is mandatory to balance multiple messages
    sleep(0.1)  
