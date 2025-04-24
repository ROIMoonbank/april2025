from flask import Flask
from waitress import serve
import os
import logging
import random

app = Flask(__name__)
logger = logging.getLogger('waitress')
logger.setLevel(logging.DEBUG)

@app.route("/")
def index():
  randomnum = random.randint(1, 100000)/100
  return "Your Bank Account Balance is: $" + str(randomnum) + "!\n"

@app.route("/version")
def version():
  return "ROI Moonbank Demo 1.0\n"

@app.route("/hello")
def hello():
  return "Hello - welcome to Moonbank\n"

if __name__ == "__main__":
  serve(app,host="0.0.0.0",port=int(os.environ.get("PORT", 8080)))