import asyncio
from time import sleep


async def hello3seconds():
    print('start hello3seconds')
    sleep(3)
    print('hello, 3s')


async def main():
    print('hello')
    task1 = asyncio.create_task(hello3seconds())

    print('world')

    # await hello3seconds()


if __name__ == '__main__':
    asyncio.run(main())
