from google.cloud import storage
import json
import re

bucket_name = "retail-data-bucket-01"
blob_name = "running-warehouse/2026-02-16.json"

client = storage.Client()
bucket = client.bucket(bucket_name)
blob = bucket.blob(blob_name)

shoes = json.loads(blob.download_as_text())

fixed_list = []
for shoe in shoes:
    fixed_model_number = re.sub(r"\n", "", shoe['model_number']).strip()
    shoe['model_number'] = fixed_model_number 
    fixed_list.append(shoe)

try:
    blob.upload_from_string(
        data = json.dumps(fixed_list, indent=2),
        content_type='application/json'
    )
    print("upload complete")
except Exception as e:
    print("failed: ", e)


