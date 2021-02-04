from flask import Flask
from flask import request
from flask import Response
import subprocess

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def respond():
    subprocess.run(["service", "flask_updater", "start"])
    return Response(status=200)


if(__name__ == '__main__'):
    app.run(host="0.0.0.0", port="4567")
