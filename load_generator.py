import asyncio
from time import time

import requests

BASE_URL = 'http://localhost:5000'


def get_requests(num):
    t0 = time()
    for i in range(num):
        requests.get(BASE_URL + '/')
    t1 = time()
    print(t1 - t0)


async def get_long_requests():
    t0 = time()
    requests.get(BASE_URL + '/long/')
    t1 = time()
    print(t1 - t0)


async def send_requests_asynchronously():
    tasks = []
    for _ in range(4):
        tasks.append(asyncio.create_task(get_long_requests()))


if __name__ == '__main__':
    # get_requests(1000)
    asyncio.run(send_requests_asynchronously())
    # get_long_requests()

