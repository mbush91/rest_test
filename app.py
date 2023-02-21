from flask import Flask, request
import logging as log

log.basicConfig(filename="test.log",level=log.INFO)

app = Flask(__name__)

@app.route('/')
def hello():
	log.info("hello")
	return "Hello World!"

@app.route('/huh')
def all():
	log.info("huh")
	return "anything!"


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)
