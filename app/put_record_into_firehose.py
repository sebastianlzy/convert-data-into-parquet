import datetime
import json
import random
import boto3
import base64

client = boto3.client('firehose')
DELIVERY_STREAM_NAME = "put-kinesis-firehose-to-s3"
count = 2882


def get_data():
    return {
        'COUNT': count,
        'EVENT_TIME': datetime.datetime.now().isoformat(),
        'TICKER': random.choice(['AAPL', 'AMZN', 'MSFT', 'INTC', 'TBV']),
        'PRICE': round(random.random() * 100, 2)
    }


def convert_to_byte(message):
    ascii_message = message.encode('ascii')
    return base64.b64encode(ascii_message)


def main():
    response = client.put_record(
        DeliveryStreamName=DELIVERY_STREAM_NAME,
        Record={
            'Data': convert_to_byte(str(get_data()))
        }
    )
    print(response)


while True:
    main()
    count = count+1
    print(count)
