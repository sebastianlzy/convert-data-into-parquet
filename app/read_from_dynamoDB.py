import boto3
import json
from boto3.dynamodb.types import TypeDeserializer
import decimal

DYNAMODB_TABLE_NAME = "amazon_review_1000"
db_table = boto3.resource('dynamodb').Table(DYNAMODB_TABLE_NAME)
dynamodb_client = boto3.client('dynamodb', region_name="us-east-1")


def read_from_dynamodb():
    return dynamodb_client.get_item(
        TableName=DYNAMODB_TABLE_NAME,
        Key={
            "product_category": {"S": "Electronics"},
            "star_rating": {
                "N": "1"
            },
        }
    )


def ddb_deserialize(r, type_deserializer = TypeDeserializer()):
    return type_deserializer.deserialize({"M": r})


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return str(o)
        return super(DecimalEncoder, self).default(o)


def lambda_handler(event, context):
    records = read_from_dynamodb()
    print(json.dumps(records["Item"], indent=4))

    amazon_review = ddb_deserialize(records["Item"])
    print(json.dumps(amazon_review, cls=DecimalEncoder, indent=4))
    return {'statusCode': 200}


lambda_handler({}, {})