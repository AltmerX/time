from flask import Flask
import time
app = Flask(__name__)

@app.route("/")
def timeSinceEpoch():
    return time.time()

if __name__ == "__main__":
    app.run()
