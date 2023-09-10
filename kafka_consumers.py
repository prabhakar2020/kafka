"""
@Author: Prabhakar
@Date: Sept 10, 2023
Description: File to fetch/ stream messages from Kafka topics
""" 
from json import loads  
from kafka import KafkaConsumer   
my_consumer = KafkaConsumer(  
    'my_group',  
     bootstrap_servers = ['localhost : 9092'],  
     auto_offset_reset = 'earliest',  
     enable_auto_commit = True,  
     group_id = 'consumer_group1',  
     value_deserializer = lambda x : loads(x.decode('utf-8'))  
     )  

for message in my_consumer:  
    # print (message.__dir__())
    # msg = message.value  
    # collection.insert_one(message)  
    print(message.value, message)
    print ("_"*25)
    print (f"""
    Topic : {message.topic}
    Value : {message.value}
    Headers : {message.headers}
    Partition : {message.partition}
    Timestamp : {message.timestamp}
    Checksum : {message.checksum}
    Serialized_key_size : {message.serialized_key_size}
    Serialized_value_size : {message.serialized_value_size}
    Serialized_header_size : {message.serialized_header_size}
    """)