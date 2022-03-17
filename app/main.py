import json
import awswrangler as wr
import pandas as pd
import os


# import requests


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    S3_PATH = "s3://convert-data-into-parquet/amazon_reviews/parquet/"
    # filename = "file1.parquet"
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, 'amazon-review-1000.csv')
    df = pd.read_csv(file_path)

    # data = {
    #     "product_name": ["Keyboard", "Mouse", "Monitor", "CPU", "Speakers", pd.NaT],
    #     "Unit_Price": [500, 200, 5000, 10000, 250.50, 350],
    #     "No_Of_Units": [5, 5, 10, 20, 8, pd.NaT],
    #     "Available_Quantity": [5, 6, 10, 0, pd.NaT, pd.NaT],
    #     "Available_Since_Date": ['11/5/2021', '4/23/2021', '08/21/2021', '09/18/2021', '01/05/2021', pd.NaT]
    # }
    #
    # df = pd.DataFrame(data)

    print(df)

    wr.s3.to_parquet(
        df=df,
        path=S3_PATH,
        dataset=True,
        partition_cols=['product_category', 'star_rating'],
        database='default',  # Athena/Glue database
        table='amazon-review-1000'  # Athena/Glue table
    )

    return {
        "statusCode": 200,
        "body": json.dumps({
            "df": df,
            # "location": ip.text.replace("\n", "")
        }),
    }


lambda_handler({}, {})
