try:
  import unzip_requirements
except ImportError:
  pass

import json
import numpy as np

def handler(event, context):
    requestBody = json.loads(event['body'])
    body = {
        "message": np.__version__,
        "input": requestBody['data']
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response