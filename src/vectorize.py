try:
  import unzip_requirements
except ImportError:
  pass

import json
import requests
from PIL import Image
from io import BytesIO
import numpy as np
from keras.applications.inception_resnet_v2 import InceptionResNetV2

def handler(event, context):
    requestBody = json.loads(event['body'])

    resnet_model = InceptionResNetV2(include_top=False, pooling='avg')
    url = requestBody['url']
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    resized = img.resize((299,299))
    array = np.array(resized)
    


    response = {
        "statusCode": 200,
        "body": json.dumps(array.shape)
    }

    return response