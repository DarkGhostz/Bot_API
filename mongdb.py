import requests
import json
url = "https://sa-east-1.aws.data.mongodb-api.com/app/data-aaagr/endpoint/data/v1/action/findOne"

payload = json.dumps({
    "collection": "<COLLECTION_NAME>",
    "database": "<DATABASE_NAME>",
    "dataSource": "Cluster0",
    "projection": {
        "_id": 1
    }
})
headers = {
  'Content-Type': 'application/json',
  'Access-Control-Request-Headers': '*',
  'api-key': 'VpuvbLbL96M2VFhPy1EMv678h80ngLmJgbxtNoi9Y7mijDV2KZPvOE7K3cMM248l', 
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
