from flask import Flask
import time
import sys

app = Flask(__name__)

@app.route("/")
def timeSinceEpoch():
    return str(time.time())

if __name__ == "__main__":
    app.run(port=sys.argv[1])
