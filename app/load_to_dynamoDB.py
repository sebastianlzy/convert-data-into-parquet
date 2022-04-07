import boto3
import json
import os
import pandas as pd

DYNAMODB_TABLE_NAME = "amazon_review_1000"

S3_PATH = "s3://convert-data-into-parquet/amazon_reviews/parquet/"
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'amazon-review-1000.csv')

db_table = boto3.resource('dynamodb').Table(DYNAMODB_TABLE_NAME)

def save_to_dynamodb(record):

    return db_table.put_item(
        Item=record)


def lambda_handler(event, context):

    df = pd.read_csv(file_path)
    rows = json.loads(df.to_json(orient="values"))

    records = []

    for cols in rows:
        print(cols)
        record = {
            "customer_id": cols[0],
            "review_id": cols[1],
            "product_id": cols[2],
            "product_parent": cols[3],
            "product_title": cols[4],
            "product_category": cols[5],
            "star_rating": int(cols[6]),
            "helpful_votes": cols[7],
            "total_votes": cols[8],
            "verfied_purchase": cols[9],
            "review_headline": cols[10],
            "review_body": cols[11],
            "review_date": cols[12],
            "marketplace": cols[13],
            "year": cols[14],

        }
        records.append(record)
        result = save_to_dynamodb(record)

        print(record)

    return {'statusCode': 200}


lambda_handler({}, {})