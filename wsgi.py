import socket
from datetime import datetime
from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    data=socket.gethostname()+": "+str(datetime.now())
    with open("/mnt/logfile", "w") as file:
        file.write(data)
    return data


if __name__ == "__main__":
    application.run()
