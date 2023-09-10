# ✨ Kafka setup ✨

## Installation of docker
You must install Docker with the steps mentioned in below<br/>
Install Docker Desktop on [Mac](https://docs.docker.com/desktop/mac/install/).<br/>
Install Docker Desktop on [Windows](https://docs.docker.com/desktop/windows/install/).<br/>
Install Docker on [Linux](https://docs.docker.com/engine/install/ubuntu/)<br/>

## Kafka setup via Docker on local machine
### Installation of Zookeeper and run on docker
Apache Kafka uses Apache ZooKeeper for distributed coordination, leader election, broker discovery, configuration management, topic and partition management, and health monitoring, making it an essential component for Kafka's operation and reliability. Use the following command to run it on docker container
<br/>`Note: By default zookeeper run on 2181 port. You can map choose host port as per your requirement`<br/>
`docker run -it -p <HOST PORT>:<CONTAINER PORT> zookeeper`

```sh
docker run -it -p 2181:2181 zookeeper
```

### Run apache Kafka on docker
Apache Kafka is an open-source distributed streaming platform for handling real-time data feeds, designed for scalability, fault tolerance, and durability. It is used in various applications for processing and analyzing streaming data.
`docker run -it -p 9092:9092 -e KAFKA_ZOOKEEPER_CONNECT=<YOUR Machine PRIVATE IP>:2181 -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://<YOUR Machine PRIVATE IP>:9092 -e KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR=1 confluentinc/cp-kafka`

```
docker run -it -p 9092:9092 -e KAFKA_ZOOKEEPER_CONNECT=192.168.137.1:2181 -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://192.168.137.1:9092 -e KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR=1 confluentinc/cp-kafka
```
```
Note: By default apache kafka run on 9092 port
```
To get private of your local machine, use the following command
`ipconfig /all`

![image](https://github.com/prabhakar2020/kafka/assets/7165155/de21d7a1-7880-4dd9-b68f-feef0450032f)

