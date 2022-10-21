from typing import Optional

from beanie import Document, init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import FastAPI


class Greeting(Document):
    message: str


async def init():
    # Create Motor client
    client = AsyncIOMotorClient(
        "mongodb://mongo-admin:mongo-password@mongo:27017"
    )

    # Initialize beanie with the Product document class and a database
    await init_beanie(database=client.backend, document_models=[Greeting])


app = FastAPI(on_startup=[init])

@app.get("/")
async def hello(name: str = "hello world"):
    return name

@app.post("/")
async def create(name: str = "world"):
    message = Greeting(message=f"Hello {name}!")
    await message.save()
    return message

@app.get("/all")
async def get_all():
    greetings = await Greeting.find().to_list()
    return greetings