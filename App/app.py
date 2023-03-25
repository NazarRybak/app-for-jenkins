from flask import Flask 


app = Flask(__name__) #екземпляр Flask


@app.route('/')  #декоратор маршруту для URL-адреси

def hello_world():
	return 'Hello, thats my little web-app!'
