from flask import Flask
import logging as log

log.basicConfig(filename="/log/test.log",level=log.INFO)

app = Flask(__name__)

@app.route('/')
def hello():
	log.info("hello")
	return "Hello World!"

@app.route('/*')
def anything():
	log.info("anything")
	return "anything!"


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)
