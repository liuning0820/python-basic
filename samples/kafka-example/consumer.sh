#!/bin/bash
export CLOUDKARAFKA_BROKERS="dory-01.srvs.cloudkafka.com:9094,dory-02.srvs.cloudkafka.com:9094,dory-03.srvs.cloudkafka.com:9094"
export CLOUDKARAFKA_USERNAME="28xk7pdt"
export CLOUDKARAFKA_PASSWORD="TcoeSxwRnH0LiVrZmeTyGV0CeDaCgUo7" # Password can be found in the Details view in for your CloudKarafka instance.
export CLOUDKARAFKA_TOPIC="28xk7pdt-demo" # Topic should be the same as your username followed by a dash before the topic.

python3 consumer.py