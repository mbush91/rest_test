from flask import Flask, request
import logging as log

log.basicConfig(filename="test.log",level=log.INFO)

app = Flask(__name__)

@app.route('/')
def hello():
	log.info("hello")
	return "Hello World!"

@app.route('/<path:text>')
def all():
	# j = request.get_json()
	# log.info("get: %s"%str(j))
	return "anything!"


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)
