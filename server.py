import boto3
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    with open("/mnt/mybucket/fastapi-test.txt", "w") as f:
        f.write("Hello World")

    return {"message": "Hello World"}


@app.get("/botoclient")
def botoclient():
    s3 = boto3.client(
        "s3",
        endpoint_url="http://minio:9000",
        aws_access_key_id="minioadmin",
        aws_secret_access_key="minioadmin",
    )

    # Get the fastapi-test.txt file from the s3 bucket
    response = s3.get_object(Bucket="test", Key="fastapi-test.txt")
    return response["Body"].read().decode("utf-8")
