import os
import boto3
import pytest
import json
from moto import mock_aws

# Set environment variables before importing lambda_function
os.environ["AWS_ACCESS_KEY_ID"] = "testing"
os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
os.environ["AWS_SECURITY_TOKEN"] = "testing"
os.environ["AWS_SESSION_TOKEN"] = "testing"
os.environ["AWS_DEFAULT_REGION"] = "us-east-1"
os.environ["DYNAMODB_TABLE"] = "cv-visitor-counter"

from lambda_function import lambda_handler

@pytest.fixture
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    # Already set at module level for import safety, but good to keep fixture style
    pass

@pytest.fixture
def dynamodb_setup(aws_credentials):
    with mock_aws():
        dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
        table = dynamodb.create_table(
            TableName="cv-visitor-counter",
            KeySchema=[{"AttributeName": "id", "KeyType": "HASH"}],
            AttributeDefinitions=[{"AttributeName": "id", "AttributeType": "S"}],
            BillingMode="PAY_PER_REQUEST"
        )
        yield table

def test_lambda_handler_increment(dynamodb_setup):
    """Test succesful increment of visitor counter."""
    # First call
    response = lambda_handler({}, {})
    assert response["statusCode"] == 200
    body = json.loads(response["body"])
    assert body["count"] == 1
    assert response["headers"]["Access-Control-Allow-Origin"] == "https://cv.aws10.dcoletasix2a.cat"

    # Second call
    response = lambda_handler({}, {})
    assert response["statusCode"] == 200
    body = json.loads(response["body"])
    assert body["count"] == 2

def test_lambda_handler_error(aws_credentials):
    """Test error handling when DynamoDB is not available (mocked without table creation)."""
    with mock_aws():
        # Do not create table, so update_item should fail
        response = lambda_handler({}, {})
        assert response["statusCode"] == 500
        body = json.loads(response["body"])
        assert "error" in body
