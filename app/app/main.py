import logging
from asyncio import get_event_loop

from app import handlers  # noqa
from app.core.bot import run
from app.core.config import settings
from app.core.db import connect_to_db

logging.basicConfig(level=logging.DEBUG if settings.DEBUG else logging.INFO)

if __name__ == '__main__':
    loop = get_event_loop()
    db_ready = loop.run_until_complete(connect_to_db())

    if db_ready:
        # Start bot
        run(loop)
    else:
        print('Start error!')
