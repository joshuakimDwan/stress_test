import threading
from time import sleep, time
from flask import request
from flask import Flask
import os


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/long/')
def long():
    t0 = time()
    order = request.args.get('order')
    thread_id = threading.get_ident()
    print('{}번째 받았다!, process_id: {} thread_id: {}'.format(order, os.getpid(), thread_id))
    count = 0
    for i in range(10000000):
        count += 1
    t1 = time()
    print(t1 - t0)
    return 'Hello, 3s'


if __name__ == '__main__':
    app.run()
