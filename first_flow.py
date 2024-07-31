import asyncio

from prefect import flow
from prefect import task


@task
async def subtask():
    print("Subtask")
    await asyncio.sleep(5)


@flow
async def my_flow(i: int):
    print("Doing something long running")
    await asyncio.sleep(20)
    await subtask()
    return "Test"
