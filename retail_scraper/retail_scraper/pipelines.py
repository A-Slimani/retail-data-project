from google.cloud import storage
from datetime import date
import json
import os

class GCSUploadPipeline:
    
    def __init__(self, bucket_name, credentials_path, file_format='json'):
        self.bucket_name = bucket_name
        self.gcs_credentials_path = credentials_path
        self.items = []


    @classmethod
    def from_crawler(cls, crawler):
        return cls (
            bucket_name=crawler.settings.get('GCS_BUCKET_NAME'),
            credentials_path=crawler.settings.get('GCS_CREDENTIALS_PATH')
        )

    def process_item(self, item, spider):
        self.items.append(dict(item))


    def close_spider(self, spider):
        if not self.items:
            spider.logger.info("No items to upload")
            return

        filename = f"{date.today()}.json"

        folder = spider.name
        blob_path = f"{folder}/{filename}"

        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = self.gcs_credentials_path

        client = storage.Client()
        bucket = client.bucket(self.bucket_name)
        blob = bucket.blob(blob_path)

        blob.upload_from_string(
            json.dumps(self.items, indent=2),
            content_type='application/json'
        )

        spider.logger.info(f"Uploaded {blob_path} to gs://{self.bucket_name}")

