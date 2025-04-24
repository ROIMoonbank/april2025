from flask import Flask
from waitress import serve
import os
import logging
import random
from google.cloud import storage

app = Flask(__name__)
logger = logging.getLogger('waitress')
logger.setLevel(logging.DEBUG)

@app.route("/")
def index():
  randomnum = random.randint(1, 100000)/100
  return "Your Bank Account Balance is: $" + str(randomnum) + "!\n"

@app.route("/listfiles")
def listfiles():
  # get a list of files in the gcs bucket gs://roi-mb-feb2025-emea-bucket
  returnmessage=""
  bucket_name="roi-mb-feb2025-emea-bucket"
  storage_client = storage.Client()
  bucket = storage_client.bucket(bucket_name)
  print(f"Successfully connected to bucket: gs://{bucket_name}")
  blobs = bucket.list_blobs() # You can also specify a prefix: bucket.list_blobs(prefix="some/folder/")
  count = 0
  for blob in blobs:
      returnmessage=returnmessage+f"- {blob.name} (Size: {blob.size} bytes)\n"           
  return returnmessage
  
@app.route("/version")
def version():
  return "ROI Moonbank Demo 1.0\n"

@app.route("/hello")
def hello():
  return "Hello - welcome to Moonbank\n"

if __name__ == "__main__":
  serve(app,host="0.0.0.0",port=int(os.environ.get("PORT", 8080)))