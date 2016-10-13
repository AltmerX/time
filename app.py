from flask import Flask
import time
import sys
import os

app = Flask(__name__)

@app.route("/")
def timeSinceEpoch():
    return str(time.time())

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0',port=port)
