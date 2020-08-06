from asyncio import sleep

from gino import Gino

from .config import settings

db = Gino()


async def connect_to_db() -> bool:
    for _ in range(2):
        try:
            await db.set_bind(settings.SQLALCHEMY_DATABASE_URI)
        except ConnectionRefusedError:
            await sleep(5)
        else:
            return True
