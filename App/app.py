from flask import Flask 
import signal

def handler(signum, frame):
    raise Exception("Times out!")

app = Flask(__name__) #екземпляр Flask

signal.signal(signal.SIGALRM, handler)
signal.alarm(15)
@app.route('/')  #декоратор маршруту для URL-адреси

def hello_world():
	return 'Hello, thats my little web-app!'
try:
    app.run(debug=True)
except Exception as ex:
    print("Error: ", ex)